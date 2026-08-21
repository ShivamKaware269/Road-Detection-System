import cv2
import numpy as np

video =cv2.VideoCapture("road_car_view.mp4")

while True:
    ret,or_frame=video.read()
    if not ret :
        video =cv2.VideoCapture("road_car_view.mp4")
        continue

    frame=cv2.GaussianBlur(or_frame,(5,5),0)

    # Converting the frame from BGR to HSV color space for better color segmentation
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_y=np.array([18,94,140])
    upper_y=np.array([48,255,255])
    
    # White -> Yellow color mask & Black -> other color mask
    mask=cv2.inRange(hsv,lower_y,upper_y)
    edges=cv2.Canny(mask,74,150)
    
    # Scan the edge image and connect line pixels into straight line segments
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    
    # Check if any lines were found in the current frame
    if lines is not None:
        for line in lines:

            # Flatten the line coordinates into 4 numbers: (x1, y1) start, (x2, y2) end
            coords = line.ravel()

            # Ignore the upper half of the screen (sky, trees, oncoming horizon) Only draw lines located in the bottom road section
            if coords[1] > 300 and coords[3] > 300:
                # Draw a bright green line over the road
                cv2.line(frame,(coords[0],coords[1]),(coords[2],coords[3]),(0,255,0),3)
    
    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    key=cv2.waitKey(25)
    
    if(key==27):
        break

video.release()
cv2.destroyAllWindows()
