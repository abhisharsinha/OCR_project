# Trying models with different configuration

aocr train --no-resume --num-epoch 1  --batch-size 64 --target-embedding-size 15 ./datasets/small-data.tfrecords
aocr train --no-resume --num-epoch 1  --batch-size 32 ./datasets/small-data.tfrecords
aocr train --no-resume --num-epoch 1  --batch-size 64 ./datasets/small-data.tfrecords
aocr train --no-resume --num-epoch 1  --batch-size 32 ./datasets/small-data.tfrecords
aocr train --no-resume --num-epoch 1  --batch-size 64 ./datasets/small-data.tfrecords
aocr train --no-resume --num-epoch 1  --batch-size 32 ./datasets/small-data.tfrecords