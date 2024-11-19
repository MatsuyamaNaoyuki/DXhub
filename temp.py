
import torch

print('GPU の利用状況 :', torch.cuda.is_available())
print('CUDA のバージョン :', torch.version.cuda)
print('cuDNN のバージョン :', torch.backends.cudnn.version())


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
A = torch.randn(3, 5)
A = A.to(device)

print(A.get_device())