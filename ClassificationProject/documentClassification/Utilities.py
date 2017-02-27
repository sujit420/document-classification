'''
Created on 27-Feb-2017

@author: sujit_kumar_mishra
'''
import pandas
from sklearn.externals import joblib


class Utilities(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def loadCSV(self,filename):
        trainigData = filename
        df = pandas.read_csv(trainigData, delimiter=',', encoding='cp1252',na_values="NaN")
        print 'CSV data loaded in memory'
        return df
    
    def pickle_model(self,classifier, modelName):
        with open(modelName, 'wb') as fid:
            joblib.dump(classifier, fid)
        print 'Pickle Saved'
        
    def unpickle_model(self,modelName):
        trainModel = None
        with open(modelName, 'rb') as inputFile:
                trainedModel = joblib.load(inputFile)
        print 'Pickle loaded in memory'      
        return trainedModel
        
    