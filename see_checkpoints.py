import tensorflow as tf
tf.enable_eager_execution()

data_path = "checkpoints/model.ckpt-4200.data-00000-of-00001"
index_path = "checkpoints/model.ckpt-4200.index"
meta_path = "checkpoints/model.ckpt-4200.meta"
chk_path = "checkpoints/model.ckpt-4200"

# from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file


# data = tf.data.TFRecordDataset([data_path])
# print_tensors_in_checkpoint_file(file_name=chk_path, tensor_name='', all_tensors=False)

# for row in data.take(10):
# 	print(row)

# data = tf.data.TFRecordDataset([index_path])
# for row in data.take(10):
# 	print(row)

# data = tf.data.TFRecordDataset([meta_path])
# for row in data.take(10):
# 	print(row)

for e in tf.train.summary_iterator("checkpoints/events.out.tfevents.1574637650.myPC"):
    # for v in e.summary.value:
        # if v.tag == 'loss' or v.tag == 'accuracy':
    pass

print(e == "summaries")