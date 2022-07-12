import cv2 as cv
import numpy as np

class Video():
    
    def __init__(self, videoId: int):
        self._cap = cv.VideoCapture(videoId)
        if not self._cap.isOpened():
            raise Exception(f'Video {videoId} cannot be opened')
        
    def getImage(self):
        while True:
            ret, frame = self._cap.read()

            # exit while loop
            if not ret:
                break

            cv.imshow('One Frame', frame)

            if cv.waitKey(1) == ord(' '):
                return frame


    
if __name__ == '__main__':
    video = Video(0)
    video.getImage()