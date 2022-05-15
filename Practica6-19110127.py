import numpy as np 
import cv2 
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)
cap.set(3, 300)
#cap.set (4, 300)


redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)

redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)


blueBajo1 = np.array([95, 100, 20], np.uint8)
blueAlto1 = np.array([145, 255, 255], np.uint8)


greenBajo1 = np.array([35, 100, 20], np.uint8)
greenAlto1 = np.array([75, 255, 255], np.uint8)

while True:
    
  ret,frame = cap.read()
  
  if ret==True:
      
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
    maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
    maskRed = cv2.add(maskRed1, maskRed2)
    
    maskRedvis = cv2.bitwise_and(frame, frame, mask= maskRed)
    
    cv2.imshow('frame', frame)
    cv2.imshow('maskRed', maskRed)
    cv2.imshow('maskRedvis', maskRedvis)
    if cv2.waitKey(30) & 0xFF == ord('m'):
      break
    
cap.release()
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
cap.set(3, 300)

while True:
    
  ret,frame = cap.read()
  
  if ret==True:
      
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    maskBlue = cv2.inRange(frameHSV, blueBajo1, blueAlto1)
    
    maskBluevis = cv2.bitwise_and(frame, frame, mask= maskBlue)
    
    cv2.imshow('Original', frame)
    cv2.imshow('maskBlue', maskBlue)
    cv2.imshow('maskBluevis', maskBluevis)
    if cv2.waitKey(30) & 0xFF == ord('m'):
      break
    
cap.release()
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
cap.set(3, 300)

while True:
    
  ret,frame = cap.read()
  
  if ret==True:
      
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    maskGreen = cv2.inRange(frameHSV, greenBajo1, greenAlto1)
    
    maskGreenvis = cv2.bitwise_and(frame, frame, mask= maskGreen)
    
    cv2.imshow('Original', frame)
    cv2.imshow('maskGreen', maskGreen)
    cv2.imshow('maskGreenvis', maskGreenvis)
    if cv2.waitKey(30) & 0xFF == ord('m'):
      break
    
cap.release()
cv2.destroyAllWindows()
