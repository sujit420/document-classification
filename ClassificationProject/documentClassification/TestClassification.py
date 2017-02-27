'''
Created on 27-Feb-2017

@author: sujit_kumar_mishra
'''
from documentClassification.Predict import Predict
from documentClassification.TrainModel import TrainModel


class TestClassification(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def test(self,modelName):
        numberOfTestCases = eval(raw_input("Enter number of sentences: "))
        sentenceList = []
        for number in range(numberOfTestCases):
            sentenceList.append(raw_input("Enter "+str(number+1)+" sentence : "))
        self.predict(sentenceList, modelName)    
        
            
    def predict(self,sentenceList,modelName):
        predict = Predict()
        predict.predict(modelName, sentenceList)
        
    def train(self,modelName,fileName):
        trainModel = TrainModel()
        trainModel.train(fileName, modelName)
        
test = TestClassification()
test.train("NewClassifier.pkl", "/home/sujit_kumar_mishra/workspace/TXT2CSV/output.csv")
test.test( "NewClassifier.pkl")

        