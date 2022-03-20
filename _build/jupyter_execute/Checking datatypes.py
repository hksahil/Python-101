#!/usr/bin/env python
# coding: utf-8

# ## Checking datatypes

# ### Data Types in Python,Pandas and Numpy

# |       | Python      | Pandas | Numpy     |
# | ---       | ---        |    ----   |          --- |
# | integer      | int      | int64       | int_,int8,int16,int32,int64   |
# | float      | float   | float64        | float_,float16,float32,float64      
# | string      | str      | object       | string_   |
# | boolean      | bool   | bool        | bool_      |

# ### Note

# - No date datatype is present in python
# - Extra Datatypes in Pandas:datetime64,timedelta[ns],category
# - Extra Datatypes in Python:list,tupple,set,dictinary

# In[1]:


# Dataframe for testing purposes
import pandas as pd
import numpy as np

df=pd.DataFrame({'Name':['Sahil', 'Sonia', 'Sourav', 'Vishal'],
        'Age':[20, 21, 19, 18]})

# Series for testing purposes
series1=pd.Series([1,2,3])

# Numpy Array for testing purposes
arr = np.array([1,2,3])


# In[2]:


df


# In[3]:


series1


# In[4]:


arr


# ### Checking datatype

# In[5]:


# For basic Python data types -> only type can be used
type('a') # <class 'str'>
type(1) # <class 'int'>
type(1.0) # <class 'float'>
type(1.9) # <class 'float'>
type([1,2,3]) # <class 'list'>
type([1,2,3,'sahil']) # <class 'list'>
type(True) # <class 'bool'>
type(('a','b')) # <class 'tuple'>
type({'a':'b'}) # <class 'dict'>


# For other things like Numpy,Pandas(Series,Dataframe)
    # We can use both type() and .dtype ( and .dtypes() also )
    # type(numpy arr | series | df) will tell the type of container
    # .dtype -> will tell us the datatype of elements inside it,which is useful
    # .dtypes -> will tell datatype of entire dataframe columns

# For numpy array
type(arr) # numpy.ndarray
arr.dtype # int32

# For Series
type(df.Name) # pandas.core.series.Series
type(df.Age) # pandas.core.series.Series
df.Name.dtype # object
df.Age.dtype # 'int64'

# For Dataframe
type(df) # pandas.core.frame.DataFrame
df.dtypes


# ### Summary

# - For Python's inbuilt basic datatypes
#     - type()
# - For numpy and Pandas columns/series/dataframes
#     - .dtype and .dtypes() will tell type of elements (int,object,float)
#     - type() will tell type of container (series,nparray,dataframe)
