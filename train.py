import torch
from model import get_model
from torch.utils.data import DataLoader
import os
from animal_keypoint.utils import collate_fn
from animal_keypoint.engine import train_one_epoch,evaluate
from customdataset import ClassDataset,train_transform

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

KEYPOINTS_FOLDER_TRAIN = 'D:\\petpets\\train'
KEYPOINTS_FOLDER_TEST = 'D:\\petpets\\valid'
save_path = 'D:\\pt'
dataset_train = ClassDataset(KEYPOINTS_FOLDER_TRAIN, transform=train_transform(), demo=False)
dataset_test = ClassDataset(KEYPOINTS_FOLDER_TEST, transform=None, demo=False)

data_loader_train = DataLoader(dataset_train, batch_size=4, shuffle=True, collate_fn=collate_fn)
data_loader_test = DataLoader(dataset_test, batch_size=4, shuffle=False, collate_fn=collate_fn)

model = get_model(num_keypoints = 15,num_classes=3)
model.to(device)

params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.001, momentum=0.9, weight_decay=0.0005)
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.3)
num_epochs = 100

checkout=True
# Run model
best_loss = float('inf')
best_loss_classifier = float('inf')
best_loss_box_reg = float('inf')
best_loss_keypoint = float('inf')
best_loss_objectness = float('inf')
best_loss_rpn_box_reg = float('inf')
best_epoch = -1
os.makedirs(f'{save_path}',exist_ok=True)
for epoch in range(num_epochs):
    loss_dict = train_one_epoch(model, optimizer, data_loader_train, device, epoch, print_freq=100)
    loss = loss_dict.meters['loss'].global_avg
    loss_classifier = loss_dict.meters['loss_classifier'].global_avg
    loss_box_reg = loss_dict.meters['loss_box_reg'].global_avg
    loss_keypoint = loss_dict.meters['loss_keypoint'].global_avg
    loss_objectness = loss_dict.meters['loss_objectness'].global_avg
    loss_rpn_box_reg = loss_dict.meters['loss_rpn_box_reg'].global_avg
    lr_scheduler.step()
    
    if loss < best_loss:
        best_loss = loss
        torch.save(model.state_dict(), os.path.join(save_path, 'best_loss.pt'))
    if loss_classifier < best_loss_classifier:
        best_loss_classifier = loss_classifier
        torch.save(model.state_dict(), os.path.join(save_path, 'best_loss_classifier.pt'))
    if loss_box_reg < best_loss_box_reg:
        best_loss_box_reg = loss_box_reg
        torch.save(model.state_dict(), os.path.join(save_path, 'best_loss_box_reg.pt'))
    if loss_keypoint < best_loss_keypoint:
        best_loss_keypoint = loss_keypoint
        torch.save(model.state_dict(), os.path.join(save_path, 'best_loss_keypoint.pt'))
    if loss_objectness < best_loss_objectness:
        best_loss_objectness = loss_objectness
        torch.save(model.state_dict(), os.path.join(save_path, 'best_loss_objectness.pt'))
    if loss_rpn_box_reg < best_loss_rpn_box_reg:
        best_loss_rpn_box_reg = loss_rpn_box_reg
        torch.save(model.state_dict(), os.path.join(save_path, 'best_loss_rpn_box_reg.pt'))
    
    if loss < best_loss or loss_classifier < best_loss_classifier or loss_box_reg < best_loss_box_reg or loss_keypoint < best_loss_keypoint or loss_objectness < best_loss_objectness or loss_rpn_box_reg < best_loss_rpn_box_reg:
        best_epoch = epoch

    os.makedirs(f'{save_path}\\epoch',exist_ok=True)
    os.makedirs(f'{save_path}\\5epoch',exist_ok=True)
    torch.save(model.state_dict(), f'{save_path}\\epoch\\keypointsrcnn_weights_{epoch}.pth')
    if epoch%5==0:
        torch.save(model.state_dict(), f'{save_path}\\5epoch\\keypointsrcnn_weights_{epoch}.pth')
    
# Save model weights after training
torch.save(model.state_dict(), 'keypointsrcnn_weights_final.pth')