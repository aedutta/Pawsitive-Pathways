import cv2
import numpy as np

def filter_for_brown(frame):
    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define HSV range for brown
    # Hue range for brown might start from orange and go up to some part of red
    # Saturation is kept medium to high to avoid capturing low-saturation (greyish) colors
    # Value (brightness) is kept low to capture the darker shades that are typical of brown
    lower_hsv = np.array([10, 100, 20])  # These are example values; adjust as needed
    upper_hsv = np.array([20, 255, 120])  # These are example values; adjust as needed
    # Threshold the HSV image to get only the brown colors
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result

def process_video(video_source=0):
    cap = cv2.VideoCapture(video_source)
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if we've reached the end of the video or if there's an error

        # Apply filtering to detect brown color
        filtered_frame = filter_for_brown(frame)

        # Display the resulting frame
        cv2.imshow('Brown Filtered Frame', filtered_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop if 'q' is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

process_video(0)
