import numpy as np
import pandas as pd
from math import exp
from sklearn.model_selection import train_test_split
class LR:
 def __init__(self):
      df = pd.read_csv("heartdp.data")
      df.columns= ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
      self.X = df.iloc[:,[2,9,11,12]]
      self.Y = df['num']
      self.coef = [0.0 for i in range(len(self.X.iloc[0])+1)]
      count = 0
      for i in self.Y:
         if i>0:
             self.Y[count] = 1

         count = count +1
      self.coef = self.coefficients(self.X,0.1,50)
      self.ypred = []
      

      

 #prediction function
 def predict(self,row, coefficients):
	 yp = coefficients[0]
	 for i in range(len(row)):
		 yp += coefficients[i + 1] * row[i]
	 return 1.0 / (1.0 + exp(-yp))

 def coefficients(self,A, L, I):
     for n in range(I):
         for i in range(len(self.X)):
             yp = self.predict(self.X.iloc[i],self.coef)
             error = self.Y.iloc[i]-yp
             self.coef[0] = self.coef[0]+L*error*yp*(1-yp)
             for j in range(len(self.X.iloc[i])):
                 self.coef[j+1] = self.coef[j+1]+ L*error*yp*(1-yp)*self.X.iloc[i][j]
     return self.coef

 def fit(self,x2,y2):
      x2 = x2.iloc[:,[2,9,11,12]]
      for i in range(0,len(x2)):
        self.ypred.append(round(self.predict(x2.iloc[i],self.coef)))
      return self.ypred



    

