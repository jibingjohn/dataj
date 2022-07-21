#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


jdata = pd.read_csv(r"C:\Users\JOBIN\Downloads\1. Weather Data.csv")


# In[19]:


jdata


# In[21]:


jdata.head()


# In[22]:


jdata.shape


# In[23]:


jdata.index


# In[24]:


jdata.columns


# In[25]:


jdata.dtypes


# In[31]:


jdata["Weather"].unique()
#in  a column, it shows uniques values


# In[33]:


#total no of unique vales in each column
data.nunique()


# In[34]:


#total no of non null values in each column
jdata.count()


# In[35]:


#in column, shows all unique values with their count
jdata["Weather"].value_counts()


# In[36]:


jdata.info()


# In[37]:


#1. Unique "Wind Speed" values in data


# In[39]:


jdata.head(4)


# In[40]:


jdata["Wind Speed_km/h"].nunique()


# In[41]:


jdata["Wind Speed_km/h"].unique()


# In[42]:


#2. Number of times weather is exactly clear


# In[43]:


jdata["Weather"].value_counts()


# In[46]:


data[data.Weather=='Clear']
#filtering


# In[47]:


#groupby
jdata.groupby("Weather").get_group("Clear")


# In[48]:


#times when "Wind speed exactly 4km/hr


# In[55]:


jdata[jdata["Wind Speed_km/h"] == 4]


# In[56]:


#blank spaces ( null values)


# In[59]:


jdata.isnull().sum()


# In[60]:


#rename "Weather" to "Weather condition"


# In[66]:


jdata.rename(columns = {"Weather" : "Weather condition"})


# In[62]:


jdata.head()


# In[67]:


#for permanent changes
jdata.rename(columns = {"Weather" : "Weather condition"}, inplace = True)


# In[68]:


jdata.head()


# In[69]:


#mean visibility
jdata.Visibility_km.mean()


# In[72]:


#std deviation Pressure
jdata.Press_kPa.std()


# In[74]:


#variance of "Relative humidity"
jdata["Rel Hum_%"].var()


# In[75]:


#instances when "snow" was recorded
jdata.head()


# In[78]:


jdata[jdata["Weather condition"] == "Snow"]


# In[79]:


#instances when word "snow" used
jdata[jdata["Weather condition"].str.contains("Snow")]


# In[81]:


# instances when wind above 24 and visibiity 25


# In[86]:


jdata[(jdata["Wind Speed_km/h"]>24) & (jdata["Visibility_km"] ==25)]


# In[87]:


#mean vaue of each column against each "Weather condition"


# In[88]:


jdata.groupby("Weather condition").mean()


# In[89]:


# max n min of each column against each "weather condition"


# In[91]:


jdata.groupby("Weather condition").min() 


# In[92]:


jdata.groupby("Weather condition").max()


# In[93]:


# instances when "weather is clear" or " visibility above 40"


# In[96]:


jdata[(jdata["Weather condition"] == "Clear") | (jdata["Visibility_km"]>40)]


# In[97]:


#instance where weather is clear and rel humidity >50 or visibility above 30


# In[103]:


jdata[(jdata["Weather condition"]== "Clear") & (jdata["Rel Hum_%"]>50) | (jdata["Visibility_km"]>30)]


# In[ ]:




