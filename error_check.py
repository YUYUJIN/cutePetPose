import cv2
import os
import glob
import json
PATH = 'D:/petpets/'
img_path = glob.glob(os.path.join(PATH, '*','images','*'))
label_path = glob.glob(os.path.join(PATH, '*','labels','*'))
error_files = {'error_files':[],'bbox':[], 'keypoint':[],'image_size':[]}
count = 0
for img,label in zip(img_path,label_path):
    # 이미지 크기
    name = img.split('/')[-1]
    image = cv2.imread(img)
    height, width, _ = image.shape
    
    # bbox 좌표
    with open(label, 'r') as f:
        json_data = json.load(f)
    bbox = json_data['bboxes'][0]
    keypoint = json_data['keypoints'][0]
    x1 = bbox[0]
    y1 = bbox[1]
    x2 = bbox[2]
    y2 = bbox[3]
    if x1<0 or y1<0 or x2>width or y2>height:
        error_files['keypoint'].append(keypoint)
        error_files['image_size'].append([height,width])
        error_files["error_files"].append([img,label])
        error_files["bbox"].append(bbox)
        print(name)
        
    if count%100==0:
        if 'train' in label:
            print(f'train {count}/{len(label_path)}')
        elif 'val' in label:
            print(f'validation {count}/{len(label_path)}')
    count+=1
with open(f'../error.json', 'w') as f:
    json.dump(error_files, f)

error_num = len(error_files['error_files'])
print(f'error file {error_files}    error num : {error_num}')
for err_img,bbox,keys in zip(error_files['error_files'],error_files["bbox"],error_files['keypoint']):
    img_path = err_img[0]
    label_path = err_img[1]
    img = cv2.imread(img_path)
    height,width,_ = img.shape
    img = cv2.resize(img,(int(width/2),int(height/2)))
    img = cv2.rectangle(img, (int(bbox[0]/2), int(bbox[1]/2)), (int(bbox[2]/2), int(bbox[3]/2)), (255, 255,0),3)
    for key in keys:
        img = cv2.circle(img, (int(key[0]/2), int(key[1]/2)), 5, (0, 0, 255))
    cv2.imshow('error', img)
    cv2.waitKey(0)
    