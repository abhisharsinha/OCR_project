import os
import cv2
import matplotlib.pyplot as plt

path = "real_data"
file = open("annotations.txt", "w")

# Resize images to 300x40 and write filenames to a file
# Sorting dir list to write filenames in sorted order
for img_name in sorted(os.listdir(path)):
	# Add filename to the annotations file
	print(img_name, "  ", file=file)
	image = cv2.imread(os.path.join(path, img_name))
	# Replace original images with resized images
	cv2.imwrite(os.path.join(path, img_name), cv2.resize(image, (300,40)))

file.close()