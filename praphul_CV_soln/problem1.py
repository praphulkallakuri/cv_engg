#!usr/bin/env python
import cv2
import sys  
import numpy as np
# print(sys.version)
# print(cv2.__version__)

font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 0, 0)
thickness = 1
fontscale=1

def detect_circles(path):
    image = cv2.imread(path)
    output = image.copy()
    height, width = image.shape[:2]
    maxradius = int(1.5*(width/12)/2)
    minradius = int(0.5*(width/12)/2)
    gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(image=gray, method=cv2.HOUGH_GRADIENT, 
                            dp=1, 
                            minDist=15, 
                            param1 = 50,
                            param2 = 30, 
                            minRadius = minradius, 
                            maxRadius = maxradius)

    if circles is not None:
        detected_circles = np.uint16(np.around(circles))

        #x,y is the center of circle and r is the radius

        for (x,y,r) in detected_circles[0, :]:
            print(x,y)
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.putText(output, str(r), (x,y), font, fontscale,color,thickness,cv2.LINE_AA, False)
            cv2.circle(output, (x, y), 1, (0, 0, 255), 3)

        cv2.imshow('circles',output)
        cv2.imwrite('circles.jpg', output)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        print ('Circles not found in the image')

if __name__ == '__main__':
    detect_circles('/home/slayer/CV_Engg/model_top_view.png')