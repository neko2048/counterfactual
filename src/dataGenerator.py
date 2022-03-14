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

    def getSex(self, age):
        sex = np.full(shape=age.shape, fill_value=-1)
        uniqueAge = np.unique(age)
        for uniqueValue in uniqueAge:
            uniqueIdx = np.where(age == uniqueValue)
            count = 0
            while count < int(len(age)/25/2):
                sex[uniqueIdx[0][count]] = 1
                count += 1
        return sex

    def getTreatment(self, sex, ageType):
        if ageType == -1:
            Ntreat = int(self.Nyoung * round(self.youngTreatRate, 4))
            Nuntreat = int(self.Nyoung * round(1-self.youngTreatRate, 4))

        elif ageType == 1:
            Ntreat = int(self.Nold * round(self.oldTreatRate, 4))
            Nuntreat = int(self.Nold * round(1-self.oldTreatRate, 4))

        treatment = np.full(shape=(sex.shape), fill_value=-1)
        count = 0
        for i in range(len(sex)):
            if sex[i] == 1:
                treatment[i] = 1
                count += 1
            if count == int(Ntreat/2):
                break
        count = 0
        for i in range(len(sex)):
            if sex[i] == -1:
                treatment[i] = 1
                count += 1
            if count == int(Ntreat/2):
                break
        return treatment

    def getAge(self, ageType):
        if ageType == -1:
            age = np.array([round(-x/25, 2) for x in range(1, 26)]*int(self.Nyoung/25))
            np.random.shuffle(age)
            return age
        elif ageType == 1:
            age = np.array([round(x/25, 2) for x in range(1, 26)]*int(self.Nold/25))
            np.random.shuffle(age)
            return age

    def getAgeTag(self, ageType):
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

class DataGenerator01(object):
    def __init__(self, config):
        self.Nold = config['Nold']
        self.Nyoung = config['Nyoung']
        self.oldTreatRate = config['oldTreatRate']
        self.youngTreatRate = config['youngTreatRate']

    def getCoefficient(self, candidate):
        return np.random.choice(a=candidate, size=1)[0]

    def getSex(self, age):
        sex = np.full(shape=age.shape, fill_value=0)#-1)
        uniqueAge = np.unique(age)
        for uniqueValue in uniqueAge:
            uniqueIdx = np.where(age == uniqueValue)
            count = 0
            while count < int(len(age)/25/2):
                sex[uniqueIdx[0][count]] = 1
                count += 1
        return sex

    def getTreatment(self, sex, ageType):
        if ageType == -1:
            Ntreat = int(self.Nyoung * round(self.youngTreatRate, 4))
            Nuntreat = int(self.Nyoung * round(1-self.youngTreatRate, 4))

        elif ageType == 1:
            Ntreat = int(self.Nold * round(self.oldTreatRate, 4))
            Nuntreat = int(self.Nold * round(1-self.oldTreatRate, 4))

        treatment = np.full(shape=(sex.shape), fill_value=0)#-1)
        count = 0
        for i in range(len(sex)):
            if sex[i] == 1:
                treatment[i] = 1
                count += 1
            if count == int(Ntreat/2):
                break
        count = 0
        for i in range(len(sex)):
            if sex[i] == 0:
                treatment[i] = 1
                count += 1
            if count == int(Ntreat/2):
                break
        return treatment

    def getAge(self, ageType):
        if ageType == -1:
            age = np.array([round(-x/25, 2) for x in range(1, 26)]*int(self.Nyoung/25))
            age = -age / 2
            np.random.shuffle(age)
            return age
        elif ageType == 1:
            age = np.array([round(x/25, 2) for x in range(1, 26)]*int(self.Nold/25))
            age = age / 2 + 0.5
            np.random.shuffle(age)
            return age

    def getAgeTag(self, ageType):
        if ageType == -1:
            return np.full(self.Nyoung, ageType)
        elif ageType == 1:
            return np.full(self.Nold, ageType)

    def getOutcome1(self, data, coefficient, CF=False):
        if CF:
            treatment = 1-data['T']
        else:
            treatment = data['T']
        return coefficient['A'] * data['Sex'] + \
               coefficient['B'] * treatment + \
               coefficient['D'] * data['Sex'] * treatment

    def getOutcome2(self, data, coefficient, CF=False):
        if CF:
            treatment = 1-data['T']
        else:
            treatment = data['T']
        return coefficient['A'] * data['Sex'] + \
               coefficient['B'] * treatment + \
               coefficient['C'] * data['Age'] + \
               coefficient['D'] * data['Age'] * data['Sex']

    def getOutcome3(self, data, coefficient, CF=False):
        if CF:
            treatment = 1-data['T']
        else:
            treatment = data['T']
        return coefficient['A'] * data['Sex'] + \
               coefficient['B'] * treatment + \
               coefficient['C'] * data['Age'] + \
               coefficient['D'] * data['Age'] * treatment

    def addNoise(self, yOrigin, loc=0, scale=0.1):
        return yOrigin + np.random.normal(loc=loc, scale=scale, size=(len(yOrigin), ))
