import cv2 as cv
import numpy as np

class CaptureImage():
    
    def __init__(self, videoId: int):
        self._cap = cv.VideoCapture(videoId)
        if not self._cap.isOpened():
            raise Exception(f'Video {videoId} cannot be opened')
        
    def getImage(self):
        while True:
            ret, frame = self._cap.read()

            if not ret:
                raise Exception(f'Return value is {ret}')

            cv.imshow('One Frame', frame)

            if cv.waitKey(1) == ord(' '):
                cv.destroyAllWindows()
                return frame


    
if __name__ == '__main__':
    # test code
    capture = CaptureImage(0)
    oneImage = capture.getImage()
    cv.imshow('captured image', oneImage)
    cv.waitKey()
    cv.destroyAllWindows()