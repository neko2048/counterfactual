import numpy as np
import pandas as pd
import torch as t
from torch.utils.data import Dataset

class CaseDataset(Dataset):
    def __init__(self, data, caseType):
        self.data = data
        self.T = self.data['T']
        self.Sex = self.data['Sex']
        self.Age = self.data['Age']
        self.feature = np.array(self.data[['T', 'Sex', 'Age']])
        self.y = np.array(self.data['y'+str(caseType)])
        self.yo = np.array(self.data['yo'+str(caseType)])
        self.featureCF = np.array(self.data[['T', 'Sex', 'Age']])
        self.featureCF[:, 0] = - self.feature[:, 0]
        self.yCF = np.array(self.data['y'+str(caseType)+'CF'])
        self.yoCF = np.array(self.data['yo'+str(caseType)+'CF'])
        #self.data = np.array(self.data)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return np.array(self.feature[idx]), np.array(self.y[idx])

    #def transformToTensor(self, arr):
    #    arr = t.tensor(np.array(arr)).to(t.float32)
    #    return arr

