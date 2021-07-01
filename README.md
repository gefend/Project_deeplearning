# Project_deeplearning

## Introduction
We worked with 40 classes from the “Quick, Draw!” dataset that includes labeled sketches that were drawn in less than 20 seconds and based ourselves on a project from a Kaggle competition on this dataset [argus quick draw]( https://github.com/lRomul/argus-quick-draw).
We improved the accuracy by adding a special augmentation to the sketches called “shake pen” and reached 94.9% accuracy on the test set.

## Setup
### Requirements
* Nvidia drivers, CUDA >= 9, cuDNN >= 7
* Docker, [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
Install docker and use it to build a docker image.
The docker file is supplied based on argus-quickdraw docker file.

|Library|Version|
|:-----:|:-----:|
|Python|3.6.5|
|Pytorch|1.0.0|
|pytorch-argus|0.0.6|
|cnn-finetune|0.5.1|
|tqdm|4.25.0|
|torchsummary|1.5.1|
|pretrainedmodels |0.74|

In addition, a requirments file is supplied. 

### Data
Data download [here](https://www.kaggle.com/c/quickdraw-doodle-recognition/data?select=train_simplified).
download train_simplified

refernces: https://github.com/lRomul/argus-quick-draw
