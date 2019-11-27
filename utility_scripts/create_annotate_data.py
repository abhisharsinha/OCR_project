import numpy as np

BASE_DIR = "/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/"
IMAGES_DIR = "text_renderer/output/default/"
DATA_DIR = "datasets/"
# TEST_SIZE = 12000

list_img_label = []
with open(IMAGES_DIR+"tmp_labels.txt", "r") as img_file:
	for line in img_file.readlines():
		parts = line.split(" ")
		label = " ".join(parts[1:]).rstrip()
		img_path = BASE_DIR + IMAGES_DIR + parts[0] + ".jpg"
		list_img_label.append((img_path, label))

# np.random.shuffle(list_img_label)
# training_samples = list_img_label[TEST_SIZE:]
# testing_samples = list_img_label[:TEST_SIZE]
training_samples = list_img_label

# CHANGE filenames
# train_filename = "annotations-training.txt"
train_filename = "emails-testing.txt"
with open(BASE_DIR+DATA_DIR+train_filename, "a") as f:
	for t in training_samples:
		print(" ".join(t), file=f)

# test_filename = "annotations-testing.txt"
# with open(BASE_DIR+DATA_DIR+test_filename, "a") as f:
# 	for t in testing_samples:
# 		print(" ".join(t), file=f)