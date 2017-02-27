'''
Created on 27-Feb-2017

@author: sujit_kumar_mishra
'''
from documentClassification.Utilities import Utilities


class Predict(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def predict(self, modelName, sentenceList):
        utilities = Utilities()
        predicted_class = None
        trainedModel = utilities.unpickle_model(modelName)
        counter = 0
        while counter < len(sentenceList):
            predicted_class = trainedModel.predict(sentenceList)[counter]
            counter = counter +1
            print 'Predicted class : '+str(predicted_class)
        
