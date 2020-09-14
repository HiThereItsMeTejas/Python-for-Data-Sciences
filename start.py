#!/usr/bin/env python
# coding: utf-8

# In[1]:


print "here i start!!"


# In[6]:


# panda stands for Python-based data analysis toolkit.

import numpy as np 
import matplotlib.pyplot as plt  

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 


# In[16]:


import numpy as np
import pandas as pd

#series
s = pd.Series([1,3,5,np.nan,6,8])
s


# In[17]:


#Data Frame (Hit tab for suggestions on Jupyterlab)

#setting date range
date = pd.date_range('20200202' , periods=6)

date


# In[20]:


df = pd.DataFrame(np.random.randn(6,4),index=date, columns=list('ABCD'))

df


# In[21]:


df.head()


# In[22]:


df.tail()


# In[23]:


df.head(1)  #selecting 1st row from data


# In[24]:


df.tail(2) #selecting last 2 row from data


# In[25]:


df.index


# In[26]:


df.columns


# In[28]:


df.to_numpy


# In[71]:


df.describe()


# In[ ]:





# In[ ]:





# In[ ]:




