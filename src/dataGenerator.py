import numpy as np 
import sys

class DataGenerator(object):
    def __init__(self, config):
        self.Nold = config['Nold']
        self.Nyoung = config['Nyoung']
        self.oldTreatRate = config['oldTreatRate']
        self.youngTreatRate = config['youngTreatRate']

    def getCoefficient(self, candidate):
        return np.random.choice(a=candidate, size=1)[0]

    def getSex(self, treatment):
        sex = np.full(shape=treatment.shape, fill_value=-1)
        for i in range(0, len(treatment), 2):
            sex[i] = 1
        return sex

    def getTreatment(self, ageType):
        if ageType == -1:
            return np.array([-1] * int(self.Nyoung * round(1-self.youngTreatRate, 2)) + \
                            [1] * int(self.Nyoung * round(self.youngTreatRate, 2)))
        elif ageType == 1:
            return np.array([-1] * int(self.Nold * round(1-self.oldTreatRate, 2)) + \
                            [1] * int(self.Nold * round(self.oldTreatRate, 2)))

    def getAge(self, ageType):
        if ageType == -1:
            return np.full(self.Nyoung, ageType)
        elif ageType == 1:
            return np.full(self.Nold, ageType)

    def getOutcome1(self, data, coefficient, CF=False):
        if CF:
            treatment = -data['T']
        else:
            treatment = data['T']
        return coefficient['A'] * data['Sex'] + \
               coefficient['B'] * treatment + \
               coefficient['D'] * data['Sex'] * treatment

    def getOutcome2(self, data, coefficient, CF=False):
        if CF:
            treatment = -data['T']
        else:
            treatment = data['T']
        return coefficient['A'] * data['Sex'] + \
               coefficient['B'] * treatment + \
               coefficient['C'] * data['Age'] + \
               coefficient['D'] * data['Age'] * data['Sex']

    def getOutcome3(self, data, coefficient, CF=False):
        if CF:
            treatment = -data['T']
        else:
            treatment = data['T']
        return coefficient['A'] * data['Sex'] + \
               coefficient['B'] * treatment + \
               coefficient['C'] * data['Age'] + \
               coefficient['D'] * data['Age'] * treatment

    def addNoise(self, yOrigin, loc=0, scale=0.1):
        return yOrigin + np.random.normal(loc=loc, scale=scale, size=(len(yOrigin), ))
