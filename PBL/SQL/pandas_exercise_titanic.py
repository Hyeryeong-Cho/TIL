#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np


# #### 1.데이터 불러오기
# 
# 
# 
# 

# In[109]:


df = pd.read_csv('C:/Users/Admin/Desktop/python/titanic_train.csv')


# In[4]:


df.head()


# In[9]:


df.info()


# #### 2.나이가 30살 이상 인 데이터 출력
# 
# 
# 
# 

# In[10]:


df[df['Age'] >= 30]


# #### 3. 500 번째 row까지 출력

# In[12]:


df.iloc[:500,]


# #### 4. Survived =0 이고, Age < 30 인 데이터 출력 

# In[16]:


df.columns


# In[36]:


issurvied = df['Survived']  == 0
is_age_under_30 = df['Age'] <30
df[is_age_under_30 & issurvied]


# #### 5. Survived =0 이고, Age < 30 인 사람의 Age 출력

# In[45]:


survived_under_30 =df[is_age_under_30 & issurvied]
survived_under_30[['Age']]


# ####  6. 생존한 사람들의 'Embarked'의 항목별로 count를 출력  
# ex)   
# S 204  
# C 172  
# Q 54  

# In[162]:


df[issurvied].groupby(['Embarked']).size()


# #### 7. 'Age'의 결측값을 'Age'의 평균값으로 대체하고 변경사항을 데이터프레임에 바로 적용  
# **(데이터프레임 출력 시 'Age'의 결측값이 평균값으로 변경되어야함)**

# In[164]:


df1 = df['Age'].isnull()
df[df1]


# In[165]:


#평균 구하기
#Mean = pd.DataFrame.mean(df['Age'])
#Mean = round(Mean,2)

df['Age'].fillna(df['Age'].mean(), inplace =True)


# In[167]:


df['Age'].isnull().sum()


# #### 8. 'Fare'(운임요금)이 20 이하인 사람들만 있는 데이터프레임에서  
# #### 'Age' column을 제거한 결과를 새로운 데이터프레임 'df_drop_age' 으로 생성    
# **(df_drop_age.head()를 찍으면 'Age' column이 없고 'Fare' 값이 20 이하로 이루어져 있어야 함)**  
# (df.loc[] 활용하여 1줄로 작성)
# 
# 

# In[168]:


#fare_under_20 = df[df['Fare']<20]
#df_drop_age = fare_under_20.drop(columns = ["Age"],axis =1)
df_drop_age = df.loc[df['Fare']<= 20].drop('Age',axis = 1)


# In[140]:




