# Trying models with different configuration

# aocr train --no-resume --num-epoch 50  --batch-size 64 --target-embedding-size 10 --initial-learning-rate 1 --use-gru ./datasets/small-data.tfrecords
# aocr train --no-resume --num-epoch 50  --batch-size 64 --target-embedding-size 15 --initial-learning-rate 1 --use-gru ./datasets/small-data.tfrecords
# aocr train --no-resume --num-epoch 50  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 1 --use-gru ./datasets/small-data.tfrecords
# aocr train --no-resume --num-epoch 50  --batch-size 64 --target-embedding-size 15 --attn-num-layers 3 --initial-learning-rate 1 --use-gru ./datasets/small-data.tfrecords

# aocr train --no-resume --num-epoch 50  --batch-size 64 --target-embedding-size 10 --initial-learning-rate 1 ./datasets/small-data.tfrecords
# aocr train --no-resume --num-epoch 50  --batch-size 64 --target-embedding-size 15 --initial-learning-rate 1 ./datasets/small-data.tfrecords
# aocr train --no-resume --num-epoch 50  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 1 ./datasets/small-data.tfrecords
# aocr train --no-resume --num-epoch 50  --batch-size 64 --target-embedding-size 15 --attn-num-layers 3 --initial-learning-rate 1 ./datasets/small-data.tfrecords


# aocr train --no-resume --num-epoch 25  --batch-size 64 --target-embedding-size 10 --initial-learning-rate 1 --use-gru ./datasets/email-training.tfrecords
# aocr train --no-resume --num-epoch 25  --batch-size 64 --target-embedding-size 15 --initial-learning-rate 1 --use-gru ./datasets/email-training.tfrecords
# aocr train --no-resume --num-epoch 25  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 1 --use-gru ./datasets/email-training.tfrecords
# aocr train --no-resume --num-epoch 25  --batch-size 64 --target-embedding-size 15 --attn-num-layers 3 --initial-learning-rate 1 --use-gru ./datasets/email-training.tfrecords

# aocr train --no-resume --num-epoch 25  --batch-size 64 --target-embedding-size 10 --initial-learning-rate 1 ./datasets/email-training.tfrecords
# aocr train --no-resume --num-epoch 25  --batch-size 64 --target-embedding-size 15 --initial-learning-rate 1 ./datasets/email-training.tfrecords
# aocr train --no-resume --num-epoch 25  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 1 ./datasets/email-training.tfrecords
# aocr train --no-resume --num-epoch 25  --batch-size 64 --target-embedding-size 15 --attn-num-layers 3 --initial-learning-rate 1 ./datasets/email-training.tfrecords

# Selecting aocr train --batch-size 64  --target-embedding-size 20 --use-gru for final training
# aocr train --no-resume --num-epoch 10  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 1 --use-gru ./datasets/new-train.tfrecords
# aocr train --num-epoch 5  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 1 --use-gru ./datasets/new-train.tfrecords
# aocr train --num-epoch 1  --batch-size 64  --target-embedding-size 20 --initial-learning-rate 0.005 --use-gru ./datasets/new-train.tfrecords

aocr train --num-epoch 10 --target-embedding-size 20 --use-gru --initial-learning-rate 0.01 ./datasets/train.tfrecords
