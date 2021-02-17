from Fknn import knn
from FLR  import LR
import numpy as np
import pandas as pd
from DT import dt
from sklearn.model_selection import train_test_split
class execution:
  def execute(self,inpname,outputpath):
    df = pd.read_csv(inpname)
    df.columns= ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
    X = df.iloc[:,0:13]
    Y  = df['num']
    count = 0
    for i in Y:
      if i>0:
        Y[count] = 1
      count = count +1
    x2 = X
    y2 = Y
    
    kobj = knn()
    knnp = kobj.fit(6,x2,y2)
    dtobj = dt()
    dtp = dtobj.predict(x2,y2)
    lrobj = LR()
    lrp = lrobj.fit(x2,y2)
    yfinalp = []
    for i in range(len(y2)):
     tp =0
     tn = 0
     if(knnp[i]==1):
       tp = tp+1
     else:
       tn = tn+1
     if(dtp[i]==1):
       tp = tp+1
     else:
      tn = tn+1
     if(lrp[i]==1):
       tp = tp+1
     else:
      tn = tn+1

     if(tp>=tn):
       yfinalp.append(1)
     else:
       yfinalp.append(0)
    tp = 0
    tn = 0
    for i in range(len(y2)):
     if(yfinalp[i]==y2.iloc[i]):
       tp =tp+1
     else:
       tn = tn+1
    df3 = pd.DataFrame(yfinalp)   
    df3.to_csv(outputpath)
    print("accuracy is")
    print((tp/len(y2))*100)


    

     