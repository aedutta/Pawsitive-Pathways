# main.py

import boto3
import os
import sys
from maps_api import get_directions
import ssl
from paho.mqtt import publish
import paho.mqtt.publish as publish


MQTT_BROKER = 'a253z0rjvuijrt-ats.iot.us-east-2.amazonaws.com'
MQTT_PORT = 8883
MQTT_TOPIC = 'home/senddirections'
CA_CERT = './RootCA.pem'
CLIENT_CERT = './8729273e81c21b47ccd3449169988254031ea54c63e9c85435b1ce05ee9050a4-certificate.pem.crt'
PRIVATE_KEY = './8729273e81c21b47ccd3449169988254031ea54c63e9c85435b1ce05ee9050a4-private.pem.key'

# Path to the text file you want to send
TEXT_FILE_PATH = 'robot_directions.txt'


tls_dict = {
    'ca_certs': CA_CERT,
    'certfile': CLIENT_CERT,
    'keyfile': PRIVATE_KEY,
    'tls_version': ssl.PROTOCOL_TLSv1_2,  # Ensure this matches your server configuration
}


with open(TEXT_FILE_PATH, 'r') as file:
    file_content = file.read()

def write_directions_to_file(origin, destination, output_file):
    directions_info = get_directions(origin, destination)
    if directions_info is None:
        print("Failed to get directions.")
        sys.exit(1)

    with open(output_file, 'w') as file:
        for info in directions_info:
            instruction = info['instruction'].replace('<div style="font-size:0.9em">', ' ').replace('</div>', '').replace('<b>', '').replace('</b>', '')
            distance = info['distance']
            file.write(f"{instruction} - {distance}\n")

def convert_directions_to_feet(input_file, output_file):
    def convert_to_feet(distance_str):
        if 'mi' in distance_str:
            # Convert miles to feet
            return str(float(distance_str.split(' ')[0]) * 5280) + ' ft'
        return distance_str  # Already in feet

    def extract_and_convert_instructions(line):
        parts = line.split(' - ')
        instructions = parts[0].split(' ')
        direction = instructions[0]  # The action like Head, Turn, Continue

        # Identify and append the direction indicator like left, right, west, etc.
        direction_indicators = ['left', 'right', 'west', 'east', 'straight']
        for word in instructions:
            if word.lower() in direction_indicators:
                direction += f" {word}"
                break

        distance = convert_to_feet(parts[1])
        return f"{direction} {distance}"

    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            formatted_line = extract_and_convert_instructions(line)
            file.write(formatted_line + '\n')

def remove_extra_newlines(input_file, output_file=None):
    # If no output file is specified, overwrite the input file
    if output_file is None:
        output_file = input_file

    with open(input_file, 'r') as file:
        # Read all lines and filter out any that are just whitespace
        lines = [line for line in file if line.strip()]

    with open(output_file, 'w') as file:
        file.writelines(lines)


def text_to_speech(text_file_path, output_bucket, output_prefix):
    # Initialize AWS clients
    polly_client = boto3.client('polly')
    s3_client = boto3.client('s3')

    # Read text from file and split into lines
    with open(text_file_path, 'r') as file:
        lines = file.readlines()

    # Convert each line to speech
    for i, line in enumerate(lines):
        # Convert text to speech
        response = polly_client.synthesize_speech(
            Text=line.strip(),
            OutputFormat='mp3',
            VoiceId='Salli'
        )

        # Save audio to a temporary file
        temp_file_path = f'/tmp/output_{i}.mp3'
        with open(temp_file_path, 'wb') as audio_file:
            audio_file.write(response['AudioStream'].read())

        # Upload audio to S3
        s3_key = f'{output_prefix}/output_{i}.mp3'
        s3_client.upload_file(temp_file_path, output_bucket, s3_key)

        # Clean up temporary file
        os.remove(temp_file_path)





if __name__ == "__main__":
    origin = "Champaign,IL"
    destination = "Urbana, IL"
    output_file = "directions.txt"
    final_output_file = "robot_directions.txt"
    output_bucket_name = "directionsaudio"
    output_file_key = "audio_output_directions"
    write_directions_to_file(origin, destination, output_file)
    convert_directions_to_feet(output_file, final_output_file)
    remove_extra_newlines(final_output_file)
    text_to_speech(output_file, output_bucket_name, output_file_key)
    
    publish.single(MQTT_TOPIC, payload=file_content, qos=1,
               hostname=MQTT_BROKER, port=MQTT_PORT,
               tls=tls_dict)
    print("Text file has been sent.")
   



