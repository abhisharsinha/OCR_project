import cv2
import os

BG_DIR = "text_renderer/data/bg/"
print(os.listdir())
for file in os.listdir(BG_DIR):
	img = cv2.imread(BG_DIR+file)
	row, col, _ = img.shape
	row_m = row//6
	col_m = col//6
	for i in range(6):
		for j in range(6):
			tmp = img[i*row_m:(i+1)*row_m, j*col_m:(j+1)*col_m, :]
			cv2.imwrite(BG_DIR+"_"+str(i)+str(j)+file, tmp)

