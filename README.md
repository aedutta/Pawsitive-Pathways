# Hack Illinois 2024 Hardware Hack 
In 36 hours, we created Pawsitive Pathways: an autonomous robot dog that helps people go from point A to B.
<div align="center">
    <img src="https://cdn.discordapp.com/attachments/821034983811448887/1211292780878626876/IMG_1079.jpg?ex=65edab4f&is=65db364f&hm=e08194c72284f8486d5ff1b0422a9a3d67b89b403517d405253c427926ab4c3e" alt="Image Description" width="30%" height="auto">
</div>
With Pawsitive Pathways, we aim to help those visually impaired gain independence and safety on the road. Recognizing the challenges they face, our team envisioned a solution that combines robotics, computer vision, and autonomous navigation to create a reliable guide for the visually impaired.

## What it does
Pawsitive Pathways is an autonomous ‘service dog’ equipped with a camera that leverages computer vision to detect crosswalks. Using live video feedback from the Raspberry Pi camera, computer vision is used to detect the sides and middle of the lane, and adjust motor speed to turn the robot in the right direction and guide the user through the path.  Integrated with the Google Maps API, the system provides real-time instructions to the robot dog, guiding users from Location A to Location B. An accompanying mobile app communicates essential information to the user through audio commands, ensuring a seamless and secure journey across crosswalks. 

## How we built it 
We built Pawsitive Pathways through a combination of hardware and software integration. The robot guides a disabled person through walkways using computer vision. The Raspberry Pi transmits live video data as frame-by-frame images to be processed on our computer. Using OpenCV, we used Canny Edge Detection and Hough transforms to create the lane lines and overlay them on the original image. We then calculate the middle of the lane using the average of their points, generate a deviation variable, and use it as a proportion to power each motor. The larger the deviation, the larger the turn, and by checking whether the deviation is negative or positive, the robot can turn in the correct direction. We also integrated the Google Maps API into our project to extract paths from one location to the other and guide the robot. The directions received from the API were also used to provide real-time audio navigation for the person using the app. 

## Challenges we ran into
During the development process, we encountered several challenges from familiarizing ourselves with John Deere machinery to fine-tuning the computer vision algorithms for accurate crosswalk detection. Until 1 pm on Saturday, our Raspberry Pi wasn’t working, which resulted in a late starting time for hardware development and didn’t allow us to do as much testing as we had hoped. Integrating the robotic hardware with the software also posed logistical challenges that required innovative solutions. We used AWS and MQTT Client to allow our code to interact and share data. Additionally, ensuring seamless communication between the mobile app and the robot dog, in regard with generating and playing the audio files in our application, presented hurdles that our team worked diligently to overcome.

## Accomplishments that we're proud of
We successfully implemented lane detection and generating a midline. The robot is able to move completely autonomously and process live video footage by communication with our computer through the IllinoisNet network. We implemented code to turn the robot based on how deviated the middle of the detected lane is from the robots centerline. We also successfully used the Google Maps API to get direction, which is converted to turn data and distance values, based on a start and end location, as well as implementing AWS text-to-speech to generate audio messages indicating what direction the robot is taking them from. 

## What we learned
We learned more about how to program with Raspberry Pi. While some of us have had Arduino experience before, none of us have worked with a Raspberry Pi in the past, so we learned a lot about RealVNC, real-time video capture, and the camera module and motor module features on the Raspberry Pi. None of us have ever done a hardware-style hack nor completely worked on both the hardware and software of a project, so we learned a lot about working with the intersection of both fields. Additionally, our team had very limited experience with AWS Services, yet we were able to develop an entire environment that connected three completely different technologies. Using input from sensors with the pi we were able to broadcast information to our AWS Cloud Server and use the software we wrote to generate audio files. These audio files would then be sent to the Flutter app which is further detailed in the next section with next steps.

## What's next for Pawsitive Pathways
In the future, we are looking to improve the fps for the camera and improve our lane detection software. With more time, we hope to implement hysteresis, more customizable and generalized thresholds for various settings, and a larger instruction set for what the robot should do when a lane is not detected. We also want to make better use of the ultrasonic sensors to implement pole detection, sign detection for safely crossing roads, and other obstacle-detection software. We currently have a completed Flutter app that can output helpful audio to the user, but are working on connecting our AWS environment with the app which will allow our robot to issue voice commands and vibrations to indicate obstacles. 
