import numpy as np
import pandas as pd
from math import exp
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
class dt:
    def __init__(self):
        df = pd.read_csv("heartdp.data")
        df.columns= ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
        self.X = df.iloc[:,0:13]
        self.Y = df['num']
# mapping target values to 0 and 1
        count = 0
        for i in self.Y:
           if i>0:
             self.Y[count] = 1
           count = count +1
    
    def predict(self,x2,y2):
            clf=RandomForestClassifier(n_estimators=100)
            #clf = DecisionTreeClassifier()
            clf = clf.fit(self.X,self.Y)
            yp = clf.predict(x2)
            return yp
