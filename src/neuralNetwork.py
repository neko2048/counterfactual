from sklearn.model_selection import train_test_split
import numpy as np 
import torch as t
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.linearLayer = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),
            #nn.Linear(256, 512),
            #nn.LeakyReLU(),
            #nn.Linear(512, 256),
            #nn.LeakyReLU(),
            nn.Linear(64, 1),
            )

    def forward(self, x):
        x = self.linearLayer(x)
        return x


def trainLoop(dataLoader, model, optimizer, lossFn, dev):
    size = len(dataLoader.dataset)
    model = model.train()
    trainLoss = 0
    numTrainedData = 0
    for batchIdx, (trainX, trainY) in enumerate(dataLoader):
        # ========== Get Prediciton and Loss (Forward) ========== 
        trainX, trainY = trainX.float().to(dev), trainY.float().to(dev)
        prediction = model(trainX)
        prediction = prediction.squeeze(1)
        loss = lossFn(prediction, trainY)

        # backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        trainLoss += loss
        numTrainedData += len(trainX)
    return trainLoss

def evaluate(model, inputData, dev, turnToNumpy=True):
    model = model.eval()
    yPred = model(t.from_numpy(inputData).float().to(dev))
    if turnToNumpy:
        yPred = yPred.cpu().detach().numpy()
    return yPred

def RMSE(prediction, target):
    return np.sqrt(np.mean((np.array(prediction) - np.array(target))**2))