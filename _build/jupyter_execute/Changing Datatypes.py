#!/usr/bin/env python
# coding: utf-8

# ## Changing Datatypes of Python's inbuilt types

# #### Changing Python's data types of values
#     - Values means single elements
#         - The data types present in python (string/float/int/list)
#         - The data types present in pandas (series/dataframe/column) can't be done by this

# #### Converting one data type to other

# In[1]:


list('sahil')


# In[2]:


list(('cat','dog'))


# In[3]:


tuple(['cat','dog'])


# In[4]:


float(1)


# In[5]:


int('001')


# - Note : Integer do not consider leading zeroes. So it automatically got removed

# In[6]:


int(15.78)


# - Note : int on floats just removes the decimal part

# In[7]:


str(1.2)


# In[8]:


str(['sahil'])


# In[9]:


str('001')

