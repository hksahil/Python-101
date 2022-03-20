#!/usr/bin/env python
# coding: utf-8

# ## Zip

# - Used to link two lists just like physical zip

# ### Syntax

# - zip(list1,list2)
#     - Takes lists
#     - Gives tupple by default

# In[1]:


list1=[1,2,3,4]
list2=['A','B','C','D']


# In[2]:


list(zip(list1,list2)) # returns iterable obj <> which is tuple by default but can be converted to list as well


# ### Unequal Length Lists

# In[3]:


id=[2,3]
name=['A','B','C','D']
list(zip(id,name))  # It will give only for 2 and 3


# In[4]:


id=[2,3,4]
name=['A','B']
list(zip(id,name))  # It will give only for 2 and 3


# #### Solution - Use zip_longest from itertools

# In[5]:


from itertools import zip_longest

id=[2,3,4,5]
name=['A','B','C']
print(list(zip_longest(id,name)))  
# assigns none for not found keys
#by default which can be replaced by other values as well using fillvalue

print(list(zip_longest(id,name,fillvalue='Not found')))  


# In[6]:


id=[2,3,4]
name=['A','B','C','D']
print(list(zip_longest(id,name)))  
# assigns none for not found keys
#by default which can be replaced by other values as well using fillvalue

print(list(zip_longest(id,name,fillvalue='Not found')))  


# ## Use case

# In[7]:


# All the if conditions can be applied since it is list comprehension


# ### Creating dictionary from list

# In[8]:


dict(zip(list1,list2))

