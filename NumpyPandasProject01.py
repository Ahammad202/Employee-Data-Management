import numpy as np
import pandas as pd

D=pd.read_excel('messy_employee_data.xlsx')
print(D)

# #For Age:
# print('Age filling with average of Age col:')
# # D['Age'].fillna((D['Age']).mean(),inplace=True)
# D['Age']=D['Age'].fillna((D['Age']).mean())
# print(D)

# #For Name:
# print('Name filing as unknown for NAN val:')
# D['Name']=D['Name'].fillna('Unknown')
# print(D)

# #For City:
# print('Toget Count of city repeatitions:')
# print(D['City'].value_counts())

# #To get Highest Repeated City:
# print(D['City'].mode())
# MostRepeatedCity=D['City'].mode()[0]
# print(MostRepeatedCity)

# #Replacing NAN city Val with MostRepeatedCity:
# print('NAN cities replaced with',MostRepeatedCity)
# D['City'].fillna(MostRepeatedCity,inplace=True)
# print(D)

# #Inf and -Inf Vals in Sal Col:

# D['Salary'].replace([np.inf,-np.inf],np.nan,inplace=True)
# # print(D)
# D['Salary'].fillna(D['Salary'].mean(),inplace=True)
# print(D)

# #Sal<0 is not realistic so replace with avg sal from Sal col:
# print('Salary filling with avg(if sal<0 then replace AVG else SameVal)' )
# D['Salary']=np.where(D['Salary']<0,D['Salary'].mean(),D['Salary'])
# print(D)

# #Dropping Duplicate vals:
# D.drop_duplicates(inplace=True)

# ##-sigma Rule:
# Sal_std=D['Salary'].std()
# Sal_mean=D['Salary'].mean()
# LowerBound=Sal_mean-(3*Sal_std)
# UpperBound=Sal_mean+(3*Sal_std)

# D1=D[(D['Salary']>LowerBound) & (D['Salary']<UpperBound)]

# print("Row count:", D.shape[0])

# # print(D.describe())
# # print(D.isnull().sum())
# # # print(D['Salary'].std())

# #Saving the Data:
# D.to_excel('Employee_Data.xlsx',index=False)
# print('Cleaned Emp Data')
# print(D)

#----------------Done------#





