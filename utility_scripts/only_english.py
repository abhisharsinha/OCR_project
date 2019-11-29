# Removes non english lines from the annotations file
# Changes the file. Make backup before running.

import re
import sys

allowed = re.compile("[a-zA-Z0-9.,:;_\[\]\-*@()]")

if not len(sys.argv) == 2:
	raise Exception("Provide filepath as argument")

try:
	lines = []
	with open(sys.argv[1], "r") as file:
		for line in file.readline():
			if allowed.match(line):
				lines.append(line)
	with open(sys.argv[1], "w") as file:
		print(*lines, sep="\n", file=file)
except:
	raise Exception("File not found")