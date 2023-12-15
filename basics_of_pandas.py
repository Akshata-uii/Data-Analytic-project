#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
df = pd.read_csv("weather_data.csv")
df


# In[2]:


df


# In[3]:


df.tail(2)


# In[4]:


df.head(4)


# In[5]:


df[["day", "event"]]


# In[6]:


df[["event"]]


# In[7]:


df[2:5]


# In[8]:


df.shape


# In[9]:


df


# In[10]:


df[df.temperature>=32]


# In[11]:


df['day'][df.temperature>=32]


# In[12]:


df[df["temperature"]==df["temperature"].max()]


# In[13]:


df


# In[14]:


df.index


# In[15]:


df.set_index('day',inplace=True)


# In[16]:


df


# In[17]:


df.loc['1/1/2017']


# In[18]:


df.reset_index(inplace=True)


# In[19]:


df


# In[20]:


df.describe()


# In[ ]:




