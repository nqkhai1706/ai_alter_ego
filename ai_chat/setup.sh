#!/usr/bin/env bash

# create and own the directories to store results locally
save_dir='save_dir'
mkdir -p $save_dir'/data/'
mkdir -p $save_dir'/nn_models/'
mkdir -p $save_dir'/results/'

# copy train and test data with proper naming
data_dir='ai_chat/data/train'

cp $data_dir'/subtitles_6M.txt' $save_dir'/data/chat.in'
cp $data_dir'/subtitles_145101.txt' $save_dir'/data/chat_test.in'
