import pytesseract 
import numpy as np
import cv2
from processimage import getSubBox
from sudoku import solve

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: python ocr.py path/to/image.png")
	imgList = getSubBox(sys.argv[1])
	sudokuGrid = getGrid(imgList)
	solution = solve(sudokuGrid)
	grid = np.zeros(shape=(9,9))
    for i, key in enumerated(sorted(solution)):
        grid[int(i/9)][i%9] = dic[key]
    print(grid)

def getGrid(imgList):
	grid = ""
	for i, j in enumerate(imgList):
		num = pytesseract.image_to_string(i)
		if not num.strip():
			grid += "."
		else:
			grid += num.strip()
	return grid