import cv2 as cv
import numpy as np


def houghTransform(strImg):
    # Getting image
    img = cv.imread(strImg)

    # Converting img to gray scale
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Applying Gaussian blur filter with 3x3 kernel
    blurImg = cv.blur(imgGray, (3,3))

    # Applying Canny for border detection over the gray image
    cannyEdges = cv.Canny(blurImg, 250, 0)
    cv.imwrite('canny_' + strImg, cannyEdges)

    # Ones we have the "edges" detected with Canny, we are going to use Hough to get the lines
    # Using Hough Probabilistic Line Transform
    houghLines = cv.HoughLinesP(cannyEdges, 1, np.pi/180, 50, minLineLength=30, maxLineGap=5)

    for line in houghLines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1,y1),(x2,y2),(0,0,255),2)
        
    cv.imwrite('houghLines_' + strImg, img)

houghTransform('campo1.jpg')
houghTransform('campo2.jpg')
houghTransform('campo3.jpg')