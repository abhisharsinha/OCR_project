# REFERENCE: https://www.tensorflow.org/guide/saved_model

# Saves predictions to a file in the following format
# <image_name> <predicted_text>
# 

import tensorflow as tf
import sys
import os

if not len(sys.argv) == 3:
    raise Exception("Provide path of savedmodel followed by image dir")

# path of saved model
# eg: ./exported-model
export_path = sys.argv[1]
img_dir = sys.argv[2] #path of image directory
if img_dir[-1] != "/":
	img_dir += "/"

file = open("img.jpg", "rb")
img = file.read()
file.close()

sess = tf.Session(graph=tf.Graph())
tf.saved_model.loader.load(sess, ["serve"], export_path)

results_file = open("results.txt", "w")

for filename in os.listdir(img_dir):
	file = open(img_dir+filename, "rb")
	image = file.read() #image is in bytes that can be feeded to the model
	file.close()
	output = sess.run(['prediction:0', 'probability:0'], feed_dict={'input_image_as_bytes:0': image})
	# output is a list with predicted text as element at position 0
	# The predicted text is in bytes. Converting to unicode sring with decode
	print(filename, output[0].decode("utf-8"), file=results_file)
	print(filename, output[0].decode("utf-8"))

results_file.close()

sess.close()
