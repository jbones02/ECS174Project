import torch.nn as nn
import torch.nn.functional as F

class EmotionCNN(nn.Module):
    def __init__(self):
        super(EmotionCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        self.fc1 = nn.Linear(64 * 12 * 12, 512)
        self.fc2 = nn.Linear(512, 8)
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        print("Shape after conv1: ", x.shape)
        x = self.pool(F.relu(self.conv2(x)))
        print("Shape after conv2: ", x.shape)
        x = self.pool(F.relu(self.conv3(x)))
        print("Shape after conv3: ", x.shape)
        x = x.view(x.size(0), -1)
        print("Shape after flattening: ", x.shape)
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.fc2(x)
        return x
