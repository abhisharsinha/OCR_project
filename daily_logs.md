23 Nov: 
1. Added corpus from Project Guttenberg, and randomly generated addresses.
2. Added open source fonts from https://www.fontsquirrel.com/
3. Added images to use as background images.

24 Nov:
1. Generated images using text_renderer.
2. Created tfrecords using aocr.

25 Nov: 
1. Started training the model.
2. Tested the model.
3. Noticed that the model was not predicting '@' symbol since the number of email addresses were rare in the dataset. So, created 2k more images with only email addresses and numbers.
4. Created tfrecords for new images.

26 Nov: 
1. Merged tfrecords to make training more inclusive.
2. Started training model.
3. Finished training the model.
4. Tested the model.

27 Nov: 
1. Exported the model.
2. Completed writing the API.

28 Nov:
1. Generated new data for training using different fonts and backgrounds.
2. Changed aocr to save loss history, train configuration and training loss plot.
3. Generated a small dataset of 900 images to try different model configurations and select the best one for traing with bigger dataset.
4. Started training small dataset using different configurations.

29 Nov- 2 Dec
Training the model.