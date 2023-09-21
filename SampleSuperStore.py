#!/usr/bin/env python
# coding: utf-8

# # Data Analysis and Business Analytic Task

# # Task 3 : Exploratory Data Analysis-Retail (SampleSuperStore) 

# In[1]:


#importing the required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sn


# In[2]:


#loading the dataset

df = pd.read_csv(r"C:\Users\vinsl\Downloads\SampleSuperstore.csv")


# In[3]:


df.sample(5)


# In[4]:


df.info()


# In[5]:


#finding the null values
df.isnull().sum()


# In[6]:


#finding the duplicate values
df.duplicated().sum()


# In[7]:


#dropping the duplicates
df.drop_duplicates(inplace= True)


# In[8]:


df['Ship Mode'].info()


# In[9]:


df['Ship Mode'].unique()


# In[10]:


df['Segment'].info()


# In[11]:


df['Segment'].unique()


# In[12]:


df['Country'].unique()


# In[13]:


df['City'].unique()


# In[14]:


df['Postal Code'].value_counts()


# In[15]:


df['Region'].unique()


# In[16]:


df['Category'].unique()


# In[17]:


df['Sub-Category'].unique()


# In[18]:


df['Sales'].describe()


# In[19]:


df['Discount'].describe()


# In[20]:


df['Profit'].describe()


# In[21]:


df.sample(3)


# In[22]:


df.drop('Country',inplace=True,axis=1)
#country column is deleted since all entries are from USA


# In[24]:


df.sample(3)


# In[25]:


# Countplot of Ship mode
sn.countplot(x = 'Ship Mode' ,data=df)
pt.title("Countplot of Shipping Mode")


# In[27]:


#countplot of segmnet
sn.countplot(x = 'Segment' ,data=df)
pt.title("Countplot of Segment")


# In[28]:


#Countplot of Region
sn.countplot(x = 'Region' ,data=df)
pt.title("Countplot of Region")


# In[29]:


#Countplot of Category
sn.countplot(x = 'Category' ,data=df)
pt.title("Countplot of Category")


# In[30]:


#countplot of Sub-Category
pt.figure(figsize=(20,5))
sn.countplot(x = 'Sub-Category' ,data=df)
pt.title("Countplot of Sub-Category")


# In[31]:


#Countplot of State
pt.figure(figsize=(20,5))
pt.xticks(rotation=90)
sn.countplot(x = 'State' ,data=df)
pt.title("Countplot of Category")


# In[32]:


#Countplot of Quantity
pt.figure(figsize=(20,5))
sn.countplot(x = 'Quantity' ,data=df)
pt.title("Countplot Quantity")


# In[33]:


#Countplot of Discount
pt.figure(figsize=(20,5))
sn.countplot(x = 'Discount' ,data=df)
pt.title("Countplot of Discount")


# In[39]:


sn.lineplot(df['Profit'])


# In[40]:


sn.lineplot(df['Sales'])


# In[36]:


#pairplot of df with category
sn.pairplot(df,hue='Category')


# In[42]:


#pairplot of df with sub-category
sn.pairplot(df,hue='Sub-Category')


# In[43]:


#pairplot of df with related to region
sn.pairplot(df,hue='Region')


# In[44]:


df.sample(3)


# In[45]:


#Ship Mode wise
Ship_Mode_wise = df.groupby(['Ship Mode'])[['Sales','Quantity','Discount','Profit']].mean()
Ship_Mode_wise


# In[46]:


Ship_Mode_wise.plot.pie(subplots=True, figsize=(25, 25),shadow=True,labels = Ship_Mode_wise.index,autopct='%.4f')


# In[47]:


#segment wise analysis
df['Segment'].value_counts()


# In[48]:


Segment_wise = df.groupby(['Segment'])[['Sales','Quantity','Discount','Profit']].mean()
Segment_wise


# In[49]:


Segment_wise.plot.pie(subplots=True, figsize=(25, 25),shadow=True,labels = Segment_wise.index,autopct='%.4f')
#pt.title("Pie diagram of Segment based on Sales,Profit,Quantity and Discount")


# In[50]:


#Statewise analysis 
State_wise = df.groupby(['State'])[['Sales','Quantity','Discount','Profit']].mean()
State_wise


# In[52]:


#State wise profit analysis
pt.figure(figsize=(20,10))
pt.grid()
(df.groupby(['State'])['Profit'].mean()).plot(kind='barh')
pt.title("State wise profit analysis")


# In[53]:


#State wise Sales analysis
pt.figure(figsize=(20,10))
(df.groupby(['State'])['Sales'].mean()).plot(kind='barh')
pt.title("State wise Sales analysis")


# In[54]:


#State wise Discount analysis
pt.figure(figsize=(20,10))
(df.groupby(['State'])['Discount'].mean()).plot(kind='barh')
pt.title("State wise Discount analysis")


# In[55]:


#State wise Quantity anaysis
pt.figure(figsize=(20,10))
(df.groupby(['State'])['Quantity'].mean()).plot(kind='barh')
pt.title("State wise Quantity analysis")


# In[56]:


#Region_wise analysis
Region_wise = df.groupby(['Region'])[['Sales','Quantity','Discount','Profit']].mean()
Region_wise


# In[57]:


Region_wise.plot.pie(subplots=True, figsize=(25, 25),shadow=True,labels = Region_wise.index,autopct='%.4f')


# In[58]:


#Category wise
Category_wise = df.groupby(['Category'])[['Sales','Quantity','Discount','Profit']].mean()
Category_wise


# In[59]:


Category_wise.plot.pie(subplots=True, figsize=(25, 25),shadow=True,labels = Category_wise.index,autopct='%.4f')


# In[60]:


#Sub-Category wise
Sub_Category_wise = df.groupby(['Sub-Category'])[['Sales','Quantity','Discount','Profit']].mean()
Sub_Category_wise


# In[61]:


# Sub-category wise Sales analysis
(df.groupby(['Sub-Category'])[['Sales']].mean()).plot(kind='bar')
pt.title("Sub-category wise Sales analysis")


# In[62]:


#Sub-category wise profit analysis
(df.groupby(['Sub-Category'])[['Profit']].mean()).plot(kind='bar')
pt.title("Sub-category wise profit analysis")


# In[63]:


#Sub-category wise discount analysis
(df.groupby(['Sub-Category'])[['Discount']].mean()).plot(kind='bar')
pt.title("Sub-category wise Discount analysis")


# In[64]:


#Sub-category wise Quantity analysis
(df.groupby(['Sub-Category'])[['Quantity']].mean()).plot(kind='bar')
pt.title("Sub-category wise Quantity analysis")


# In[65]:


df.groupby(['City'])[['Sales','Profit','Discount','Quantity']].mean()


# In[68]:


df['City'].count()


# In[84]:


top_20 = df['City'].value_counts().iloc[:20]
top_20        


# In[93]:


pt.figure(figsize=(20,10))
top_20.plot(kind='bar')
pt.title("Top 20 cities")


# #Results
# -Sales are almost same for all shipping modes but profit and discount is high for first class
# -Segment wise max profit and sales are obtained from home office items.
# State wise max sales in Wyoming and max profit in Vermont
# -Region wise south as highest sales, west has max profit. Desipte of high discount , central has very low profit.
# -Category wise max sales and profit for technology and despite max discount and sales, furniture as low profit.
# -Sub-category wise max sales and profit obtained for Copiers. Machine has good sales and discount but no profit.no of fastner purchased and discount is high but less profit

# In[ ]:





# In[ ]:




