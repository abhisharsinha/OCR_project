# Merging two tfrecords of previous training data and emails data

# REFERENCES: 
# 1.  https://stackoverflow.com/questions/50265211/how-can-i-merge-multiple-tfrecords-file-into-one-file
# 2. https://www.tensorflow.org/tutorials/load_data/tfrecord

# HOW TO USE:
# Pass 3 tfrecords filenames as cli
# Multiple tfrecords file names to merge and save into the last filename

# EXAMPLE:
# python merge_tfrecords.py train.tfrecords test.tfrecords complete.tfrecords

import sys
import tensorflow as tf
tf.enable_eager_execution()

if len(sys.argv) < 4:
	raise Exception("Enter Multiple tfrecords file names to merge and save into the last filename")

# rec1 = "/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/datasets/email-training.tfrecords"
# rec2 = "/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/datasets/training.tfrecords"
list_records = []
for rec in sys.argv[1:-1]:
	list_records.append(rec)

dataset = tf.data.TFRecordDataset(list_records)

# filename = '/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/datasets/train-complete.tfrecords

filename = sys.argv[-1]
writer = tf.data.experimental.TFRecordWriter(filename)
writer.write(dataset)
# writer.close()