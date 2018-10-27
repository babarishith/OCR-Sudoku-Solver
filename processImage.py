import cv2
import numpy as np


def getSubBox(img_path):

    img = cv2.imread(img_path, 0)
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.ones_like(img) * 255

    boxes = []
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            hull = cv2.convexHull(contour)
            cv2.drawContours(mask, [hull], -1, 0, -1)
            x,y,w,h = cv2.boundingRect(contour)
            boxes.append((x,y,w,h))

    boxes = sorted(boxes, key=lambda box: box[0])
    mask = cv2.dilate(mask, np.ones((5,5),np.uint8))

    result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    grid_boxes = [None]*81
    i,j = 8,0
    cut = 0
    for n,box in enumerate(boxes):
        x, y, w, h = box
        grid_boxes[9*i+j] = result[y+int(h*cut):y+int(h*(1-cut)), x+int(w*cut):x+int(w*(1-cut))]
        i = i - 1
        if i < 0:
            j = j + 1
            i = 8

    return grid_boxes


