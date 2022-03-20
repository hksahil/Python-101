#!/usr/bin/env python
# coding: utf-8

# ## Formatting Strings

# - Dynamic strings

# In[1]:


name='Sahil'
age=25


# ### Using .format()

# In[2]:


print('My name is {}. I am {} years old'.format(name,age))


# ### F-string - Better way !!

# - Just place f in start of string
# - You can add variables directly
# - You don't need to first convert everything to string and then do concatenation

# In[3]:


print(f"My name is {name}. I am {age} years old")


# - You can run functions on variables and evaluate or perform computation within string

# In[4]:


print(f"My name is {name.upper()}. I am {float(age+1)} years old")


# In[5]:


dict={'name':'sahil','age':25}


# In[6]:


print(f'My name is {dict['name']}. I am {dict['age']} years old')


# - Note: Error came because pythn gets confused in single quotes used in string
#     - So,always use double quotes to start and end a string

# In[17]:


print(f"My name is {dict['name']}. I am {dict['age']} years old")


# In[ ]:




