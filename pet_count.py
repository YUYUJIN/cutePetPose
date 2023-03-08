import os
import glob

BASE_PATH = 'D:\\pet'
cat=os.listdir('D:\petdataset\Training\CAT')[:12]
dog=os.listdir('D:\petdataset\Training\DOG')[:13]
count=0
pet_action = []
act = {}
for i in cat:
    pet_action.append('cat_'+i.lower())
for i in dog:
    pet_action.append('dog_'+i.lower())
path = glob.glob(os.path.join(BASE_PATH,'*','labels','*'))
total_count=0
for i in pet_action:
    cat_dog = i.split('_')[0]
    if cat_dog not in act:
        act[cat_dog] = {}
    action = i
    act[cat_dog][action] = 0
for i in path:
    pet = i.split('\\')[4].split('-')[0]
    action = i.split('\\')[4].split('-')[1]
    print(f'{total_count}/{len(path)}')
    total_count+=1
    for j in pet_action:
        p_a = j.split('_')
        if pet== p_a[0] and action==p_a[1]:
            act[j.split('_')[0]][j]+=1
dog_count = sum(act['dog'].values())
cat_count = sum(act['cat'].values())
total_count = dog_count+cat_count
print("Dog count:", dog_count)
print("Cat count:", cat_count)
print("total count:", total_count)
print("Dog dictionary:")
for key, value in act['dog'].items():
    print(f"{key}: {value}")
print("Cat dictionary:")
for key, value in act['cat'].items():
    print(f"{key}: {value}")

            
