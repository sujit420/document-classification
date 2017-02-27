'''
Created on 27-Feb-2017

@author: sujit_kumar_mishra
'''

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from documentClassification.Utilities import Utilities


class TrainModel(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.trainedModel = None
        self.vectorizer = None
        self.classifier = None
        
    def featureTransformer(self,dataframe,train=True):
        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
        X = None
        if train == True:
            X = vectorizer.fit_transform(dataframe["Document"])
        else:
            X = vectorizer.transform(dataframe["Document"])
        self.vectorizer = vectorizer
        print 'Feature transformed'
        return X
    
    def train(self,fileName,modelName):
        print 'Training started'
        lr = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, solver='newton-cg', penalty='l2', random_state=None, tol=0.0001, multi_class='multinomial')
        utilities = Utilities()
        dataframe = utilities.loadCSV(fileName)
        X = self.featureTransformer(dataframe, train=True)
        param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000] }
        clf = GridSearchCV(lr, param_grid)
        clf = clf.fit(X, dataframe["Category"])
        vec_clf = Pipeline([('tfvec', self.vectorizer), ('gridsearch', clf)])
        self.classifier = vec_clf
        best_parameters, score, _ = max(clf.grid_scores_, key=lambda x: x[1])
        print 'Training Completed with score : '+str(score)
        print 'Best training parameter selected: '+ str(best_parameters)
        utilities.pickle_model(self.classifier, modelName)
