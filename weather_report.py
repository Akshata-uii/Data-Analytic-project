#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd 
pf=pd.read_excel(r'C:\Users\I\Downloads\weather_dataset_stage1.xls')
#import the data from excel


# In[14]:


print(pf)


# In[1]:


import pandas as pd 
pf=pd.read_excel(r'C:\Users\I\Downloads\weather_dataset_stage1.xls')


# In[2]:


print(pf)


# In[1]:


import pandas as pd 
pf=pd.read_excel(r'C:\Users\I\Downloads\weather_dataset_stage1.xls')


# In[2]:


print(pf)


# In[14]:


import pandas as pd 
import datetime
pf=pd.read_excel(r'C:\Users\I\Downloads\weather_dataset_stage1.xls')
print(pf)


# In[17]:


#pf['Date ']=pd.to_datetime(pf['Date'],format='%d%m%y')
pf.dtypes


# In[45]:


#pf['Date']=pd.to_datetime(pf['Date'], format('%d/%m/%Y'),errors='ignore')


# In[37]:


#pf.dtypes


# In[38]:


#print(pf)


# In[35]:





# In[44]:


pf['Date ']=datetime.strptime(pf['Date'], '%m/%d/%Y ')


# In[49]:


pf['Date']=pd.to_datetime(pf['Date'], format'%d%m%Y')
#pf['Date ']=pd.to_datetime(pf['Date'],format='%d%m%y')


# In[62]:


import pandas as pd 
import datetime 
pf=pd.read_excel(r'C:\Users\I\Downloads\weather_dataset_stage1.xls')


# In[58]:


print(pf)


# In[59]:


pf.dtypes


# In[64]:


pf['Date'] = pd.to_datetime(pf['Date'],errors='ignore')

#pf['Date'] = pf['Date'].dt.strftime('%d-%m%Y')


# In[69]:



#pf['Date'] = pf['Date'].apply(lambda x: x.replace("'", ''))
for i in pf:
    pf[i] = pf[i].apply(lambda x: x.replace("'", ''))


# In[70]:


print(pf)


# In[72]:


pf.dtypes


# In[76]:


pf.Maximum rain per minute.unique()


# In[ ]:





# In[ ]:





# In[ ]:




