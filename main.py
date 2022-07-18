import time
import cv2 as cv
from capture_image import CaptureImage

print('hell world, my AI app')


class FrameRate:
    def __init__(self) -> None:
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


frameRate = FrameRate()
captureImage = CaptureImage(0)
oneImage = captureImage.getImage()
cv.imshow('Captured Image', oneImage)
cv.waitKey()
cv.imwrite('captured.png', oneImage)
cv.destroyAllWindows()