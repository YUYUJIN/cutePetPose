import json
import os
import glob

cat_image_list = glob.glob(os.path.join('D:\Data\Training\CAT\image', '*', '*', '*', '*.jpg'))

cat_valid = 0
cat_null = 0
cat_data = dict()

print('Collecting start!')

for image_path in cat_image_list:
    file_name = image_path.split('\\')[-2]
    pose = image_path.split('\\')[-3]
    json_path = os.path.join('D:/Data/Training/CAT/label', pose, pose, file_name + '.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        label_dict = json.load(f)
    
    image_name = image_path.split('\\')[-1]
    image_frame = image_name.split('_')[1]
    
    for frame in label_dict['annotations']:
        if frame['frame_number'] == int(image_frame):
            flag = True
            for keypoint, coord in frame['keypoints'].items():
                if coord == None:
                    flag = False
            if flag:
                cat_valid += 1
                if pose not in cat_data.keys():
                    cat_data[pose] = 1
                else:
                    cat_data[pose] += 1
            else:
                cat_null += 1
            
            if cat_valid % 1000 == 0:
                print('{} data collected'.format(cat_valid))
                print('{} data failed'.format(cat_null))

with open('./cat_data.json', 'w') as f:
    json.dump(cat_data, f, indent='\t')

with open('./cat_result.txt', 'w') as f:
    f.write('Cat data : {}, null data : {}'.format(cat_valid, cat_null))