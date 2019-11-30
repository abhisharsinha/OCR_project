# Removes non english lines from the annotations file
# Changes the file. Make backup before running.
# HOW TO USE:
# Provide filepath followed by image dir as argument

# import re
import sys
import os

# allowed = re.compile("[a-zA-Z0-9.,:;@()-]")

if not len(sys.argv) == 3:
	raise Exception("Provide filepath followed by image dir as argument")

img_dir = sys.argv[2]
img_dir = os.getcwd()+"/"+img_dir

if not img_dir[-1] == "/":
	img_dir += "/"

try:
	lines = []
	with open(sys.argv[1], "r") as file:
		for line in file.readlines():
			# if allowed.match(str(line)):
			# If ascii alphanumeric
			if all([word.isalnum() and all([ord(char) < 128 for char in word]) for word in line.split()[1:]]):
				# filenames in annotations have . before _ missing
				line = "._".join(line.rstrip().split("_"))
				lines.append(img_dir+line)
	print(len(lines), " lines written")
	with open(sys.argv[1], "w") as file:
		print(*lines, sep="\n", file=file)
except:
	raise Exception("File not found")