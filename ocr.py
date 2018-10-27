import pytesseract 
import numpy as np
import cv2
from processImage import getSubBox
from sudoku import solve
import sys

def getGrid(imgList):
    grid = ""
    for i in imgList:
        # cv2.imshow("img", i)
        # cv2.waitKey(0)
        num = pytesseract.image_to_string(i, config="--psm 10")
        if not num.strip():
            grid += "."
        else:
            char = num.strip()
            if (char.isdigit()):
                grid += num
            else:
                grid += "."
    return grid

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python ocr.py path/to/image.png")
    imgList = getSubBox(sys.argv[1])
    sudokuGrid = getGrid(imgList)
    print(sudokuGrid)
    #print(len(sudokuGrid))
    solution = solve(sudokuGrid)
    if not solution:
        print("Grid is wrong")
    else:
        grid = np.zeros(shape=(9,9))
        for i, key in enumerate(sorted(solution)):
            grid[int(i/9)][i%9] = solution[key]
        print(grid)