import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_edge_detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #Args: image, kernel size, deviation; the canny function acc automatically does this for us
    canny = cv2.Canny(blur, 50, 150)#Args: image, low threshold, high threshold
    return canny

def region_of_interest(image):
    #--- CREATE TRIANGULAR MASK ----#
    height = image.shape[0]
    #polygons = np.array([[ (0, height), (1100, height), (550, 200) ]]) #must pass an array of possible polygons ot fillPoly, so we willl create an array with just 1 polygon --> the triangle
    polygons = np.array([[ (200, height), (1100, height), (550, 250) ]])

    #create a mask the shape of the triangle
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255) #Arg: mask, shape of mask, color of mask
  
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
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0: #Left: neg. slope
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    left_fit_avg = np.average(left_fit, axis = 0) #left line slope,intercept
    right_fit_avg = np.average(right_fit, axis = 0) #same, but right line
    
    left_line = make_coordinates(image, left_fit_avg)
    right_line = make_coordinates(image, right_fit_avg)
    
    #GET MID LINE
    lx1, lx2= left_line[0], left_line[2]
    rx1, rx2= right_line[0], right_line[2]

    mx1 = lx1 + int((rx1-lx1)/2)
    mx2 = lx2 + int((rx2-lx2)/2)
    my1 = image.shape[0]
    mid_line = np.array([mx1, my1, mx2, int(my1*(3/5))])
    #print(mid_line)

    return np.array([left_line, right_line, mid_line])

#Using the slope/intercept, create lines starting from the bottom till 3/5 of the way up the image
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])


'''
image = cv2.imread('test_img.jpg') #returns image as numpy array
lane_image = np.copy(image)

canny = canny_edge_detect(lane_image)
cropped_image = region_of_interest(canny)

lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap = 5)  #Args: image, # of pixels in bin, degree of precision(in radians), threshold of min # of votes required for a line 
averaged_lines = average_slope_intercept(lane_image, lines)
line_image = display_lines(lane_image, averaged_lines)
lane_overlay_img = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1) #adds line_image matrix to og image (as weights); Arg: img1, weight, img2, weight, scalar addition

cv2.imshow('result', lane_overlay_img) #can also use cv2 instead of plt
#plt.show() 
cv2.waitKey(0) #displays image for prolonged period --> 0 means display till keypress
'''

cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read() #decodes every video frame

    canny = canny_edge_detect(frame)
    cropped_image = region_of_interest(canny)

    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap = 5)  #Args: image, # of pixels in bin, degree of precision(in radians), threshold of min # of votes required for a line 
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    lane_overlay_img = cv2.addWeighted(frame, 0.8, line_image, 1, 1) #adds line_image matrix to og image (as weights); Arg: img1, weight, img2, weight, scalar addition

    cv2.imshow('result', lane_overlay_img) #can also use cv2 instead of plt

    if cv2.waitKey(1) == ord('q'): #break if user presses q
        break

cap.release()
cv2.destroyAllWindows() 

