#! /bin/bash

mkdir data
cd data
wget http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat
mkdir bin
wget http://images.cocodataset.org/zips/train2017.zip
unzip -q train2017.zip
