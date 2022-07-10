import cv2
import numpy as np
import time

print('hell world, my AI app')

class FrameRate:
    def __init__(self) ->None:
        self._count = 0
        self._start = time.time()
    
    def tick(self) -> None:
        self._count = self._count + 1
        self._diff = time.time() - self._start

    def getFrame(self) -> float:
        self._frameRate = self._count / self._diff
        return self._frameRate

    def printFrame(self) -> None:
        print(f'count is: {self._count} frame: {self.getFrame()}')


cap = cv2.VideoCapture(2)
frameRate = FrameRate()

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # flip on x
    frame = cv2.flip(grey, 1)

    cv2.imshow('grey', frame)

    ret, frame = cv2.threshold(frame, 127, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    #print frame rate
    frameRate.tick()
    frameRate.printFrame()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

