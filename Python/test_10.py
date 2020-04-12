import cv2 as cv

def function_frame(img):
  print("Hello")
  print(img)

  #cv.imshow('Frame',img)

  if cv.waitKey(25) & 0xFF == ord('q'):
    cap.release()
    cv.destroyAllWindows()

#----------------------------------------

if __name__ == "__main__":
    cap = cv.VideoCapture("test.mp4")
    while cap.isOpened ():
      ret , frame = cap.read()
      if ret == True:
        function_frame(frame)
      else:
        break


