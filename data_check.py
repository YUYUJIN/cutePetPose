import json
import os
import glob

cat_json_list = glob.glob(os.path.join('D:/Data/Training/Label/Cat', '*', '*', '*.json'))
dog_json_list = glob.glob(os.path.join('D:/Data/Training/Label/Dog', '*', '*', '*.json'))

print('cat : {}, dog : {}'.format(len(cat_json_list), len(dog_json_list)))

exit()
cat_label = {}
cat_except = 0
for json_path in cat_json_list:
    label = json_path.split('\\')[-2]
    with open(json_path, 'r', encoding='utf-8') as f:
        temp_dict = json.load(f)
    for frame in temp_dict['annotations']:
        flag = True
        for keypoint, coord in frame['keypoints'].items():
            if coord == None:
                flag = False
        if flag:
            if label not in cat_label.keys():
                cat_label[label] = 1
            else:
                cat_label[label] += 1
        else:
            cat_except += 1
    print('{} done'.format(json_path.split('\\')[-1]))

with open('./cat_label.json', 'w') as f:
    json.dump(cat_label, f, indent="\t")

print('{} data excepted'.format(cat_except))

dog_label = {}
dog_except = 0
for json_path in dog_json_list:
    label = json_path.split('\\')[-2]
    with open(json_path, 'r', encoding='utf-8') as f:
        temp_dict = json.load(f)
    for frame in temp_dict['annotations']:
        flag = True
        for keypoint, coord in frame['keypoints'].items():
            if coord == None:
                flag = False
        if flag:
            if label not in dog_label.keys():
                dog_label[label] = 1
            else:
                dog_label[label] += 1
        else:
            dog_except += 1
    print('{} done'.format(json_path.split('\\')[-1]))

with open('./dog_label.json', 'w') as f:
    json.dump(dog_label, f, indent="\t")

print('{} data excepted'.format(dog_except))
