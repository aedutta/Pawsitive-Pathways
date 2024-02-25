from src import camera as camera_module
from src import motor as motor_module
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def autonomous(image, mx1, mx2):
    frame_center = image.shape[1] / 2
    mx_center = (mx1 + mx2) / 2
    deviation = frame_center - mx_center
    print(deviation)

    kp = 0.01
    base_speed = 0.5

    left_motor_speed = base_speed + max(0, kp*deviation)
    right_motor_speed = base_speed + abs(min(0, kp*deviation))

    motor1.forward(left_motor_speed)
    motor2.forward(right_motor_speed)


def canny_edge_detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #Args: image, kernel size, deviation; the canny function acc automatically does this for us
    canny = cv2.Canny(blur, 50, 150)#Args: image, low threshold, high threshold
    return canny

def region_of_interest(image):
    #--- CREATE TRIANGULAR MASK ----#
    height = image.shape[0]
    width = image.shape[1]
    #polygons = np.array([[ (0, height), (1100, height), (550, 200) ]]) #must pass an array of possible polygons ot fillPoly, so we willl create an array with just 1 polygon --> the triangle
    triangle = np.array([[(0, 250), (width, 250), (310, 100) ]])
    square = np.array([[(0, height), (0, 250), (width, 250), (width, height)]])

    #polygons = np.array([[ (0, height), (500, height), (550, 200) ]])

    #create a mask the shape of the triangle
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, square, 255) #Arg: mask, shape of mask, color of mask
    cv2.fillPoly(mask, triangle, 255)
  
    #----- APPLY MASK ----#
    #bitwise AND between canny img and mask --> all the white portions will include only that section of the og img
    masked_image = cv2.bitwise_and(image, mask)

    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10) #10 is line thickness
    return line_image

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            intercept = parameters[1]
            if abs(slope) <= 0.2:
                continue
            elif slope < 0: #Left: neg. slope
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
        
        left_fit_avg = np.average(left_fit, axis = 0) #left line slope,intercept
        right_fit_avg = np.average(right_fit, axis = 0) #same, but right line
        
        left_line = make_coordinates(image, left_fit_avg)
        right_line = make_coordinates(image, right_fit_avg)
        
        try:
            #GET MID LINE
            lx1, lx2= left_line[0], left_line[2]
            rx1, rx2= right_line[0], right_line[2]

            mx1 = lx1 + int((rx1-lx1)/2)
            mx2 = lx2 + int((rx2-lx2)/2)
            my1 = image.shape[0]
            mid_line = np.array([mx1, my1, mx2, 150])
            #print(mid_line)
        except:
            mid_line = np.array([0, 0, 0, 0])

        return np.array([left_line, right_line, mid_line])
    return None

#Using the slope/intercept, create lines starting from the bottom till 3/5 of the way up the image
def make_coordinates(image, line_parameters):
    try:
        slope, intercept = line_parameters
        y1 = image.shape[0]
        y2 = 150
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return np.array([x1, y1, x2, y2])
    except:
        return np.array([0, 0, 0, 0])



if __name__ == '__main__':
    motor1 = motor_module.Motor({
    "pins": {
        "speed": 13,
        "control1": 5,
        "control2": 6
    }
    })

    motor2 = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        }
    })
    '''
    total_seconds = 60
    sample_hz = 30

    camera = camera_module.Camera({
        "show_preview": True
    })
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        camera.capture()
        print(camera.image_array)

        time.sleep(max(0, 1/sample_hz -
                       (time.time() - start_time)))


    '''
    total_seconds = 200
    sample_hz = 30
    camera = camera_module.Camera({
        "show_preview": True
    })

    try:
        start_time = time.time()
        while (time.time() - start_time < total_seconds):
            camera.capture()
            frame = camera.image_array[:, :, 0:3]
            #print(frame)
            
            canny = canny_edge_detect(frame)
            cropped_image = region_of_interest(canny)
            
            lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
            averaged_lines = average_slope_intercept(frame, lines)
            line_image = display_lines(frame, averaged_lines)
            lane_overlay_img = cv2.addWeighted(frame, 0.7, line_image, 1, 1)
            
            _, mx1, _, mx2 = averaged_lines[-1]
            #print(averaged_lines[-1])
            autonomous(frame, mx1, mx2)

            cv2.imshow('result', lane_overlay_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Program interrupted")

    finally:
        cv2.destroyAllWindows()
        # Ensure motors are stopped
        motor1.stop()
        motor2.stop()
        print("Cleaned up resources and stopped motors")
