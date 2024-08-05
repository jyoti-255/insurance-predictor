#import lib
import pandas as pd
from sklearn.linear_model import LogisticRegression

#load the data
data=pd.read_csv("ai_march24.csv")
feature=data[["age"]]
target=data["have_insurance"]

#model
model=LogisticRegression()
model.fit(feature.values,target)

#predction using mathematical model
age=float(input("enter age"))
b0=model.intercept_
b1=model.coef_[0]
res=1/(1+(2.71**(-1*(b0+b1*age))))
#print(res)

if res>=0.5:
  print("yes")
else:
  print("no")