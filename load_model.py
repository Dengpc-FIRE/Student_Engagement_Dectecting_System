import os
import json
import cv2
import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
from EfficientNet import efficientnet_b0


def get_model():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    data_transform = transforms.Compose(
        [transforms.CenterCrop(48),
         transforms.Resize(45),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # load image
    # img_path = 'test_image/4.jpg'
    # assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    # img = Image.open(img_path)
    # plt.imshow(img)
    # [N, C, H, W]
    # img = data_transform(img)
    # expand batch dimension
    # img = torch.unsqueeze(img, dim=0)

    # read class_indict
    """json_path = 'class_indices.json'
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)

    with open(json_path, "r") as f:
        class_indict = json.load(f)"""

    # create model
    model = efficientnet_b0(num_classes=3).to(device)

    # load model weights
    weights_path = "D:\Privacy-Protected Classroom Participation Analysis System latest version\Student Engagement Detecting System\models\efficientnetBest_cbam 63.8%.pth"
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path, map_location=device))

    return model, data_transform
