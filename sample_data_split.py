import os
import glob
import json
import random
from sklearn.model_selection import train_test_split
import shutil

# 불러올 파일 개수
num_data = 20000

# 이미지 파일 경로 -> cat 따로 dog 따로
image_dir = 'D:/detection_cat/images'
image_paths = glob.glob(os.path.join(image_dir, '*.jpg'))

# JSON 파일 경로
json_dir = 'D:/detection_cat/labels'
json_paths = [os.path.join(json_dir, os.path.splitext(os.path.basename(path))[0]+'.json') for path in image_paths]

# 이미지 파일과 JSON 파일 경로를 묶음
data_paths = list(zip(image_paths, json_paths))

# 데이터를 무작위로 섞음
random.shuffle(data_paths)

# 불러올 데이터 개수에 맞게 데이터를 잘라냄
data_paths = data_paths[:num_data]

# train과 test 데이터로 분할
train_data_paths, test_data_paths = train_test_split(data_paths, test_size=0.2, random_state=100)

# train과 test 데이터를 저장할 디렉토리 생성
train_dir = 'D:/catdog/train'
test_dir = 'D:/catdog/test'
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# train 데이터 저장
for path in train_data_paths:
    image_path, json_path = path
    image_file_name = os.path.basename(image_path)
    json_file_name = os.path.basename(json_path)
    shutil.copyfile(image_path, os.path.join(train_dir, image_file_name))
    shutil.copyfile(json_path, os.path.join(train_dir, json_file_name))

# test 데이터 저장
for path in test_data_paths:
    image_path, json_path = path
    image_file_name = os.path.basename(image_path)
    json_file_name = os.path.basename(json_path)
    shutil.copyfile(image_path, os.path.join(test_dir, image_file_name))
    shutil.copyfile(json_path, os.path.join(test_dir, json_file_name))
