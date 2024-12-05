import time
#resnetを実装したもの
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.models import resnet18
from torch.utils.data import DataLoader
from myclass import myfunction
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
import matplotlib.pyplot as plt
import random



class ResNetRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(ResNetRegression, self).__init__()
        self.resnet = resnet18(weights=None)

        # 最初の畳み込み層を 2D Conv に変更
        self.resnet.conv1 = nn.Conv2d(
            in_channels=1, out_channels=64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1)
        )

        # BatchNorm2d を BatchNorm1d に変更する必要はありません
        self.resnet.bn1 = nn.BatchNorm2d(64)

        # 出力層を回帰問題用に変更
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, output_dim)

    def forward(self, x):
        x = x.unsqueeze(1).unsqueeze(-1)  # (batch_size, input_dim) -> (batch_size, 1, input_dim, 1)
        out = self.resnet(x)
        return out

input_dim = 17
output_dim = 5
learning_rate = 0.001
num_epochs = 300



model = ResNetRegression(input_dim=input_dim, output_dim=output_dim)
if torch.cuda.is_available():
    model.cuda()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

model_from_script = torch.jit.load('1204_twodimention/model_epoch90_20241204_145631.pth', map_location="cuda:0")

filename = "1204_twodimention/test20241203_172216.csv"
x_data,y_data = myfunction.read_csv_to_torch(filename)
x_data = x_data.to(device)
y_data = y_data.to(device)
x_mean = x_data.mean()
x_std = x_data.std()
y_mean = y_data.mean()
y_std = y_data.std()
x_change = (x_data - x_data.mean()) / x_data.std()
y_change = (y_data - y_data.mean()) / y_data.std()

model_from_script.eval()

# x_data から 1 サンプルを取得（例: 0番目のサンプル）


for i in range(10):
    sample_idx = 100  # 推論したいサンプルのインデックス
    single_sample = x_change[sample_idx].unsqueeze(0)  # (input_dim,) -> (1, input_dim)
    # 推論を行う（GPUが有効ならGPU上で実行）
    with torch.no_grad():  # 勾配計算を無効化
        prediction = model_from_script(single_sample)
    single_sample = single_sample * x_std + x_mean
    prediction = prediction * y_std + y_mean
    

# 結果を確認
print("Prediction:", prediction)
print("y:", y_change[100])