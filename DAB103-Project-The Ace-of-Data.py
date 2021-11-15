#!/usr/bin/env python
# coding: utf-8

# In[125]:


import warnings
warnings.filterwarnings("ignore")


# In[70]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[71]:


data = pd.read_csv("ITSalarySurveyEU.csv")


# In[72]:


data.head()


# In[73]:


data.isnull().sum()


# In[74]:


sns.heatmap(data.isnull(), cbar=True)


# In[75]:


data.isnull().sum()


# In[136]:


#str.strip() will remove extra space before and after column name
#str.lower() will convert all column names to lower case
#str.replace(' ', '_') will replace '<space>' in column name by '_' due to this there will be no key error
data.columns = (data.columns.str.strip().str.lower()
              .str.replace(' ', '_')
               .str.replace('&','_'))
data.head()


# In[130]:


data.isnull()


# In[131]:


sns.set_style('whitegrid')
sns.countplot(y='seniority_level', data=data)


# In[159]:


sns.set_style('whitegrid')
sns.countplot(x='lost_job', hue='gender', data=data)


# In[132]:


sns.set_style('whitegrid')
sns.countplot(y='main_language',data=data)


# In[133]:


sns.displot(data['age'])


# In[134]:


sns.set_style('whitegrid')
sns.countplot(x='gender', data=data)


# In[135]:


sns.barplot(y='seniority_level', x='age', data=data)


# In[139]:


plt.figure(figsize=(18,18))
sns.set_style('whitegrid')
sns.countplot(y='position', data=data)


# In[156]:


plt.figure(figsize=(18,18))
sns.set_style('whitegrid')
sns.countplot(y='technical_language', data=data)


# In[143]:


data.loc[317, 'total_years_of_experience'] = '15'
display(data.loc[317])


# In[145]:


data.to_csv("ITSalarySurveyEU.csv", index=False)
display(data.loc[317])


# In[147]:


data["total_years_of_experience"] = data["total_years_of_experience"].astype(str).astype(float)


# In[155]:


# Employment status by gender 
sns.barplot(y='employment_status', data=data)

