import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
class knn:
    def __init__(self):
      df = pd.read_csv("heartdp.data")
      df.columns= ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
      self.X = df.iloc[:,0:13]
      self.Y = df['num']

    # mapping target values to 0 and 1
    
    def mapping(self):
     count = 0   
     for i in self.Y:
         if i>0:
             self.Y[count] = 1
         count = count +1
    #diatance cal   
    def dis(self,E,F):
     sum = 0
     for i in range(0,13):
         sum = sum+((E[i]-F[i])**2)
     sum = sum**0.5
     return sum

    def predict(self,C,D):
     count = 0
     s = []
     c = []
     for a in range(0,len(D)):
         d1  = self.dis(C,D.iloc[a])
         s.append(d1)
         c.append(self.Y.iloc[count])
         count = count+1
     zipped_lists = zip(s, c)
     sorted_pairs = sorted(zipped_lists)
     tuples = zip(*sorted_pairs)
     s, c = [ list(tuple) for tuple in  tuples]
     c1 = c[0:self.n]
     yes = 0
     no  = 0
     for i in c1:
         if i==0:
             no = no+1
         else:
             yes = yes+1
     if(yes>no):
         return 1
     else:
         return 0

    def fit(self,n,x2,y2):
     self.n = n
     self.ypred = []
     self.y2 = y2
     for i in range(0,len(x2)):
         self.ypred.append(self.predict(x2.iloc[i],self.X))
     return self.ypred
    
    def accuracy(self):
     tp =0
     for i in range(0,len(self.ypred)):
         if self.y2.iloc[i] == self.ypred[i]:
             tp = tp+1
     return (tp/len(self.ypred))*100


