import cv2
import time
  
 
# SET THE COUNTDOWN TIMER to 5

TIMER = int(5)
  
# Open the camera
cap = cv2.VideoCapture(0)
  
while True:
     
    # Read and display each frame
    ret, img = cap.read()
    grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam_feed', grayscale)
 
    # check for the key pressed
    k = cv2.waitKey(125)
 
    # set the key for the countdown
    # to begin. press spacebar
    if k == 32:
        #store started time
        prev = time.time()
 
        while TIMER >= 0:
            ret, img = cap.read()
            #convert webcam feed to grayscale
            grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Display countdown on each frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(grayscale, str(TIMER),
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('camera', grayscale)
            cv2.waitKey(125)
 
            # current time
            cur = time.time()
 
            # calculate difference of current time and started time
            # after one second,
            # than decrease the counter
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1

        #It's time to save your photo
        else:
            ret, img = cap.read()
            grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            cv2.imshow('selfie', grayscale)
 
            # time for which image displayed
            cv2.waitKey(2000)
 
            # Save the frame as .jpg image
            cv2.imwrite('selfie2.jpg', grayscale)
 
    # Press Esc to exit
    elif k == 27:
        break
 
# release the camera
cap.release()
