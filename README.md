# Project_deeplearning

## Introduction
We worked with 40 classes from the “Quick, Draw!” dataset that includes labeled sketches that were drawn in less than 20 seconds and based ourselves on a project from a Kaggle competition on this dataset [argus quick draw]( https://github.com/lRomul/argus-quick-draw).
We improved the accuracy by adding a special augmentation to the sketches called “shake pen” and reached 94.9% accuracy on the test set.

## Setup
### Requirements
* Nvidia drivers, CUDA >= 9, cuDNN >= 7
* Docker, [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
Install docker and use it to build docker image.
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

### Preparations
Clone the repo and build docker image

```shell
git clone https://github.com/gefend/Project_deeplearning/tree/main/argus-quick-draw-master
cd argus-quick-draw
make build
```

### Data
Data download [here](https://www.kaggle.com/c/quickdraw-doodle-recognition/data?select=train_simplified).
download train_simplified

We used only 40 classes out of the classes in the origianl data. 

The following classes were used: Ambulance, Apple, Bear, Bicycle, Cactus, Camera, Carrot, Crocodile, Diamond, Dog, Ear, Eye, Flamingo, Giraffe, Helmet, House, Key, Lightning, Lion, Mermaid, Monkey, Moon, Neckless, Octopus, Onion, Panda, Pizza, Rabbit, Rainbow, Shark, Skull, Snowflake, Spider, Sun, Sword, Table, Telephone, Underwear, Whale, Zebra.

Remove all other classes csv files after downloading.

## Files in the repository
|File name|Purpose|Our modifications/additions|
|:-------:|:-----:|:-------------------------:|
|create_test_csv.py|Build a csv file for the prediction and build a csv file with the labels for the accuracy calculations|original|
|plot_results.py|plot the training results: val accuracy, val map@k,val loss, train loss, learning rate|origianl|
|choice_val_key_ids.py|split the train dataset to train, validation and test|modified: added a split to a test set|
|test_calculate_accuracy.py|Calculate the predictions accuracy on the test set|original|
|comp_shake.py|Plot the drawings with the "shake pan" augmentaion| original|
|train.py|model training|modified:to work with our data splits, reduced: 1.num of workers in the dataloader 2.train epoch size 3.max epochs 4.early stopping patience|
|predict.py|Run the model on the test set to get predictions|modified: to work with our data splits and to prodcue only one class prediction per sample|
|src/draw.py|Transform the raw data, strokes, to RGB images|modified: shake pan function was added|
|src/config.py| configuration file| modified: with our paths|
|src/datasets.py|load the validation,test and train sets| modified: to load our splits|
|src/argus_models.py|build the model| no modifications|
|src/metrics.py| define metrices| no modifications|
|src/nn_modules.py|build a model for country embedding| no modifications|
|src/transforms.py|define the data transformations| modified: added the shake pan transofrm|
|src/utils.py|utility functions|no modifications|



refernces: https://github.com/lRomul/argus-quick-draw
