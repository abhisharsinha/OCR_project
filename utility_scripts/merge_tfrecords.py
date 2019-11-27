# Merging two tfrecords of previous training data and emails data
# REFERENCES: 1.  https://stackoverflow.com/questions/50265211/how-can-i-merge-multiple-tfrecords-file-into-one-file
# 2. https://www.tensorflow.org/tutorials/load_data/tfrecord


import tensorflow as tf
tf.enable_eager_execution()

rec1 = "/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/datasets/email-training.tfrecords"
rec2 = "/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/datasets/training.tfrecords"
dataset = tf.data.TFRecordDataset([rec1, rec2])
dataset

filename = '/home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/datasets/train-complete.tfrecords'
writer = tf.data.experimental.TFRecordWriter(filename)
writer.write(dataset)
# writer.close()