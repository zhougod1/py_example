import cv2
import numpy as np

def main():
    otemp = './asserts/bg.jpg'
    oblk = './asserts/block.jpg'
    target = cv2.imread(otemp, 0)
    template = cv2.imread(oblk, 0)
    w, h = target.shape[::-1]
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    print ((y, x),(y + w, x + h))
 

if __name__ == '__main__':
    main()