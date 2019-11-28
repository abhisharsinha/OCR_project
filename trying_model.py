# https://www.tensorflow.org/guide/saved_model

import tensorflow as tf

export_path = "./exported-model"
file = open("img.jpg", "rb")
img = file.read()
file.close()
# with tf.Session(graph=tf.Graph()) as sess:
sess = tf.Session(graph=tf.Graph())
tf.saved_model.loader.load(sess, ["serve"], export_path)
# graph = tf.get_default_graph()
# print(graph.get_operations())
sess.run(['prediction:0', 'probability:0'], feed_dict={'input_image_as_bytes:0': img})

sess.close()
