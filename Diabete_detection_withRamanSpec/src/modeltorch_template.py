import numpy as np
import torch
from torch.utils.data import TensorDataset
import torch
from torch import nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()  # super(Model, self)
        self.fc1 = nn.Linear(input_size, hidden_size)
        # add non-linearity; recall ReLU is max(input, 0)
        self.snm = nn.Softmax(dim=1)
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.snm(out)
        out = self.fc2(out)
        return out


class IntANN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()  # super(Model, self)
        self.fc1 = nn.Linear(input_size, hidden_size)
        # add non-linearity; recall ReLU is max(input, 0)
        self.snm = nn.Softmax(dim=1)
        self.do1 = nn.Dropout(p=.5)
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.snm(out)
        out = self.do1(out)
        out = self.fc2(out)
        return out


class RamConv1d(nn.Module):
    def __init__(self, input_size=1, hidden_size=50, linear_hidden=14, out_size=2):
        super().__init__()
        self.conv1d = nn.Conv1d(input_size, hidden_size, kernel_size=3)
        # taking the last hidden state
        self.linear1 = nn.Linear(49900, linear_hidden)
        self.linear2 = nn.Linear(linear_hidden, out_size)

    def forward(self, seq):
        # seq shape: (10, 1, 1000)
        out = self.conv1d(seq)
        # out shape: (10, 50, 998)
        out = out.reshape(seq.size(0), -1)
        # print(out.shape)
        out = self.linear1(out)
        out = self.linear2(out)
        return out


class RamLSTM(nn.Module):
    def __init__(self, input_size=1000, hidden_size=100, out_size=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.linear = nn.Linear(hidden_size, out_size)

    def forward(self, seq):
        out, (_, _) = self.lstm(seq)
        out = out[:, -1, :]  # (B, Hout)

        out = self.linear(out)
        return out


class IntRamLSTM(nn.Module):
    def __init__(self, input_size=1000, hidden_size=100, out_size=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size,
                            batch_first=True, dropout=0.5)
        # self.linear = nn.Linear(hidden_size, hidden_s2)
        self.linear2 = nn.Linear(hidden_size, out_size)
        self.do = nn.Dropout(p=.5)
        self.relu = nn.ReLU()

    def forward(self, seq):
        out, (_, _) = self.lstm(seq)
        out = out[:, -1, :]  # (B, Hout)
        #
        # out = self.linear(out)
        out = self.relu(out)
        self.do(out)

        return self.linear2(out)


class RamConv1d_bnmx(nn.Module):
    def __init__(self, input_size=1, hidden_size=10, hidden_size2=50, linear_hidden=14, out_size=2):
        super().__init__()
        self.conv1 = nn.Conv1d(input_size, hidden_size, kernel_size=3)
        self.relu1 = nn.ReLU()
        # Convolution Layer 2
        self.conv2 = nn.Conv1d(hidden_size, hidden_size2, kernel_size=3)
        self.maxpool1 = nn.MaxPool1d(2)
        self.maxpool2 = nn.MaxPool1d(2)
        self.relu2 = nn.ReLU()

        # Fully connected layers
        self.fc1 = nn.Linear(12400, linear_hidden)
        self.fc2 = nn.Linear(linear_hidden, out_size)
        self.batchnorm1 = nn.BatchNorm1d(hidden_size)
        self.batchnorm2 = nn.BatchNorm1d(hidden_size2)
        # self.batchnorm3 = nn.BatchNorm1d(50)

    def forward(self, x):

        # Convolution Layer 1
        x = self.conv1(x)
        x = self.batchnorm1(x)
        x = self.relu1(x)
        x = self.maxpool1(x)
        # Convolution Layer 2
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.relu2(x)
        x = self.batchnorm2(x)
        # Switch from activation maps to vectors
        # x = x.reshape(-1, 24900)
        # print(x.shape)
        x = x.reshape(x.size(0), -1)
        # print(x.shape)
        # Fully connected layer 1
        x = self.fc1(x)
        x = self.relu1(x)
        # Fully connected layer 2
        x = self.fc2(x)

        return x


class RamConv1d_mx(nn.Module):
    def __init__(self, input_size=1, hidden_size=10, hidden_size2=50, linear_hidden=14, out_size=2):
        super().__init__()
        self.conv1 = nn.Conv1d(input_size, hidden_size, kernel_size=3)
        self.relu1 = nn.ReLU()
        # Convolution Layer 2
        self.conv2 = nn.Conv1d(hidden_size, hidden_size2, kernel_size=3)
        self.maxpool1 = nn.MaxPool1d(2)
        self.maxpool2 = nn.MaxPool1d(2)
        self.relu2 = nn.ReLU()
        self.drop = nn.Dropout(p=0.5)

        self.fc1 = nn.Linear(12400, 1000)
        self.fc2 = nn.Linear(1000, linear_hidden)
        self.fc3 = nn.Linear(linear_hidden, out_size)

    def forward(self, x):

        # Convolution Layer 1
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.maxpool1(x)
        # Convolution Layer 2
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.maxpool2(x)

        x = x.reshape(x.size(0), -1)

        x = self.fc1(x)
        x = self.relu1(x)

        x = self.drop(x)
        x = self.fc2(x)
        x = self.relu1(x)
        return self.fc3(x)
