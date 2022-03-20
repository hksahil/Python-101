#!/usr/bin/env python
# coding: utf-8

# ## List Slicing

# In[1]:


names=['Sahil','Sonia','Sourav','Deepak','Vishal']
age=[1,2,3]


# ### Syntax

# - names[starting index:ending index:step]
#     - starting index is inclusive
#     - ending index is exclusive , so write thing you need +1

# #### Get Indexes based on element

# In[2]:


names.index('Deepak')


# ### Traversing from left to right

# In[3]:


names[:]
# or names[0:len(names)]
# or [ i for i in names]    # we generally prefer comprehension for iterations


# ### Traversing from right to left

# In[4]:


names[::-1]
# or [i for i in names[::-1]]


# ### Getting First Element

# In[5]:


names[0]


# ### Getting Second element

# In[6]:


names[1]


# ### Getting first 3 elements

# In[7]:


names[0:3]


# ### Getting last element

# In[8]:


names[-1]


# ### Getting second last element

# In[9]:


names[-2]


# ### Getting last 3 elements

# In[10]:


names[-3:]


# ### Getting Last elements index

# In[11]:


len(names)-1


# ### Give me elements based on index

# In[12]:


# eg,give me sonia,sourav,deepak
names=['Sahil','Sonia','Sourav','Deepak','Vishal']
names[names.index('Sonia'):names.index('Vishal')]  # last index is exclusive so I wrote visal

