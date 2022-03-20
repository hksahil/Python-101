#!/usr/bin/env python
# coding: utf-8

# ## Dictionaries

# In[1]:


dict1={
    'name':"Sahil",
    'age':24,
    'gender':'Male',
    'profession':['Data Analyst','SDE','SEO']
}
dict1


# ### Get all Keys

# In[2]:


dict1.keys()


# ### Get all Values

# In[3]:


dict1.values()


# ### Get Keys+Values

# In[4]:


dict1.items()


# ### Get specific Values

# - dict1['key you want value for']

# In[5]:


dict1['name']


# In[6]:


dict1['profession'][1]


# ### Assigning/Overwritting Values

# In[7]:


dict1['name']='Sahil Choudhary'
dict1


# ### Adding new keys/values

# In[8]:


dict1['email']='officialhksahil@gmail.com'
dict1


# ### Removing key/value pair

# In[9]:


del dict1['age']
dict1


# ### Looping

# #### By default,it gives keys only

# In[10]:


for x in dict1:
    print(x)


# #### To loop through keys and values : items is the solution always

# In[11]:


for x,y in dict1.items():
    print(x,y)

