#!/usr/bin/env python
# coding: utf-8

# ## Read Elements

# In[1]:


names=['Sahil','Sonia','Sourav']
age=[10,20,30]


# ### Get first value

# In[2]:


names[0]


# ### Get last value

# In[3]:


names[-1]


# ### Getting a range

# In[4]:


names[0:2]


# ### Getting all values

# In[5]:


[i for i in names]


# In[6]:


for i in names:
    print(i)


# ### Getting values+Indexes

# In[7]:


for i,x in enumerate(names):
    print(i,x)


# ### Iterate through two lists at same time

# In[8]:


for x,y in zip(names,age):
    print(x + " is " + str(y) + " years old")

