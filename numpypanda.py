#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
n1 = np.full((2,2),10)


# In[5]:


n1


# n2 = np.arange(10,50,5) 

# In[6]:


n2 = np.arange(10,50,5)


# In[7]:


n2


# In[8]:


n3 = np.arange(100,300)


# In[9]:


n3


# In[10]:


import pandas as pd


# In[12]:


s1 = pd.Series([1,2,3,4,5,6])


# In[13]:


s1


# In[14]:


type(s1)


# In[17]:


s2 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[18]:


s2


# In[19]:


type(s2)


# In[20]:


s2[:4]


# In[21]:


pd.DataFrame({"Name":['rociala','romero','miloma'],"Marks":[50,90,100]})


# In[ ]:




