# Removes non english lines from the annotations file of public_data
# and fixes the typo in filenames

# Changes the file. Make backup before running.
# HOW TO USE:
# Provide filepath followed by image dir as argument
p

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
			# Checking that the characters are alphanumeric and english
			# isalnum() returns True for Chinese characters so checking
			# is all characters have ord < 128 ie are in ascii
			if all([word.isalnum() and all([ord(char) < 128 for char in word]) for word in line.split()[1:]]):
				# filenames in annotations have '.' missing before '_'
				line = "._".join(line.rstrip().split("_"))
				lines.append(img_dir+line)
	
	with open(sys.argv[1], "w") as file:
		print(*lines, sep="\n", file=file)
except:
	raise Exception("File not found")