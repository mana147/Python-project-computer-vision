
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from  display import Display

W = 1920//2
H = 1080//2

disp = Display(W,H)
orb = cv.ORB_create()

print (dir(orb))

#---------------------------------------------
def function_frame(img , numb ):
  img = cv.resize(img,(W,H))

  kp , des = orb.detectAndCompute(img , None)

  for p in kp:
    u,v = map (lambda x: int(round(x)),p.pt)
    cv.circle(img , (u,v) , color= (0,255,0) , radius = 3)
 
  disp.paint(img)

  #cv.imwrite("save_frame/frame%d.png" % numb, img)

  '''
  cv.imshow('Frame',img)
  print(img.shape)
  print(img)
  
  if cv.waitKey(25) & 0xFF == ord('q'):
    cap.release()
    cv.destroyAllWindows()
    f.close()
  '''
#----------------------------------------------
def function_save_frame(img ,numb ):
  cv.imwrite("save_frame/frame%d.png" % numb, img)

#----------------------------------------------
def function_save_frame_text(img , numb ):
  f = open("demo.txt", "a")
  f.write()
  
#----------------------------------------------
if __name__ == "__main__":

    #cap = cv.VideoCapture(0)
    cap = cv.VideoCapture("test.mp4")
    count = 0
    while cap.isOpened ():
      ret , frame = cap.read()

      gray =  cv.cvtColor (frame , cv.COLOR_BGR2GRAY) 
      
      if ret == True:
        function_frame(frame , count )
        #function_save_frame(frame ,count)
        #function_save_frame_text (frame ,count)

        count = count + 1 
      else:
        break
#------------------------------------------------
