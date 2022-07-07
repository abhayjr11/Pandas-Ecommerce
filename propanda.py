#!/usr/bin/env python
# coding: utf-8

# # Project Pandas : 

# In[1]:


# import pandas
import pandas as pd  
import numpy as np


# In[2]:


# load the data
data = pd.read_csv('Ecom')
data.head()

# 1. Display Top 10 Rows of The Dataset
# In[3]:


data.head(10)

# 2. Check Last 10 Rows of The Dataset
# In[4]:


data.tail(10)

# 3. Check Datatype of Each Column
# In[5]:


data.info()

# 4. Check null values in the dataset
# In[6]:


data.isna()

# 5. How many rows and columns are there in our Dataset? 
# In[7]:


print(len(data.columns),len(data))

# 6. Highest and Lowest Purchase Prices.
# In[8]:


print(min(data['Purchase Price']),max(data['Purchase Price']))

# 7. Average Purchase Price
# In[34]:


data['Purchase Price'].mean()

# 8. How many people have French 'fr' as their Language
# In[20]:


data['Language'].isin(['fr']).sum(axis=0)


# In[21]:


len(data[data['Language']=='fr'])

# 9. Job Title Contains Engineer
# In[24]:


len(data[data['Job'].str.contains('engineer',case=False)])

# 10. Find The Email of the person with the following IP Address: 132.207.160.22
# In[27]:


data[data['IP Address']=='132.207.160.22']['Email']

# 11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50
# In[62]:


len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)])

# 12. Find the email of the person with the following Credit Card Number: 4664825258997302
# In[64]:


data[data['Credit Card']==4664825258997302]['Email']

# 13. How many people purchase during the AM and how many people purchase during PM?

# In[70]:


data['AM or PM'].value_counts()

# 14. How many people have a credit card that expires in 2020?
# In[80]:


len(data[data['CC Exp Date'].str.contains('/20')])

# 15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 
# In[94]:


list=[]
for e in data['Email']:
    list.append(e.split('@')[1])
data['temp']=list
data['temp'].value_counts().head()


# In[95]:


data['Email'].apply(lambda x : x.split('@')[1]).value_counts().head()


# In[ ]:




