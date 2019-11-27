# Get alphabets to use in CHARMAP of aocr

file_path = "./text_renderer/output/default/labels.txt"

alphabet = set()

with open(file_path, "r") as f:
	for line in f.readlines():
		for char in line:
			alphabet.add(char)

print("".join(sorted(alphabet)))
print(len(alphabet), alphabet)  # --> 82 including \n


# Finding maximum label length
max_label_length = 0
largest_label = ""
with open(file_path, "r") as f:
	for line in f.readlines():
		if len(" ".join(line.split()[1:])) > max_label_length:
			max_label_length = len(" ".join(line.split()[1:]))
			largest_label = " ".join(line.split()[1:])
print(max_label_length, largest_label)

# Finding number of labels greater than threshold
THRESHOLD = 15
num_larg_labels = 0
with open(file_path, "r") as f:
	for line in f.readlines():
		if len(" ".join(line.split()[1:])) > THRESHOLD:
			num_larg_labels += 1
print("{0} labels greater than threshold {1}".format(num_larg_labels, THRESHOLD))

# Checking how many labels in the modified dataset includes @ symbol
count_at_sym = 0
num_larg_labels = 0
with open(file_path, "r") as f:
	for line in f.readlines():
		if len(" ".join(line.split()[1:])) <= THRESHOLD and '2' in line:
			count_at_sym += 1
print(count_at_sym)