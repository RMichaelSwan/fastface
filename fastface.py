import numpy as np
import cv2
import cvlib as cvl


vid = cv2.VideoCapture(0)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    faces, confidences = cvl.detect_face(frame)
    # print(faces)
  
    # Display the resulting frame
    topleft = (faces[0][0],faces[0][1])
    botright= (faces[0][2],faces[0][3])
    cv2.rectangle(frame,topleft,botright,(0,255,0),3)
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

