#!/usr/bin/env python
# coding: utf-8

# ## Changing Datatypes of Pandas inbuilt types

# - For series,dataframe,column which are datatypes present in pandas library not in python

# #### 3 options

# - .astype(int|float|str)
# - pd.to_numeric()
# - pd.to_datetime()
# 
# 
# - Use pd.numeric only if mixed col(mixed with strings or mixed with Nan's) 
# - Otherwise use astype

# In[1]:


import pandas as pd
df=pd.DataFrame({'Name':['Sahil', 'Sonia', 'Sourav', 'Vishal'],
        'Age':[20, 21, 19, 18],
        'Number':[100,200,300,400],
        'Weight':[12.2,12.4,43.4,45.1],
        'Height':[12.2,44.3,76.8,12.3]        })
df


# ### Change datatype of one/multiple columns

# In[2]:


# ASTYPE()
# Change datatype of one column:
df_new=df['Age'].astype(int)

# Change datatype of multiple columns:
df_new=df.astype({'Age': 'float64', 'Name': 'object'})

# PD.TO_NUMERIC()
# Change datatype of one column:
df['Age']=pd.to_numeric(df['Age'])

# convert just columns "Weight" & "Height"
df[["Weight", "Height"]] = df[["Weight", "Height"]].apply(pd.to_numeric)


# In[3]:


df.dtypes


# ### Select and convert float columns only

# In[4]:


float_cols = df.select_dtypes(include=['float64']) # This will select float columns only
print(list(float_cols.columns.values))
print()
print(float_cols)

for col in float_cols.columns.values:
    df[col] = df[col].astype('int64')
    
# or refer to string functions notebook


# In[5]:


df.dtypes


# ### Snippet to convert datatypes while catching the errors as well

# In[6]:


try:
        df['Age'] = df['Age'].astype(float)
except TypeError as e:
        print(e)


# ### Use case 1: Numbers as strings

# In[7]:


l=['1','2','3','4'] # String gets converted into object
df=pd.DataFrame(l,columns =['Numbers'])


# In[8]:


df


# In[9]:


df.Numbers.dtype


# In[10]:


# df['string_col']=df['string_col'].astype(int//float//string)
df['Numbers']=pd.to_numeric(df['Numbers'])


# In[11]:


df.Numbers.dtype   # DONE !!!


# ### Use case 2: Ints+Floats

# In[12]:


l=[1,2,3,4,5.5] # Note: If only one float,entire column gets converted into float
df=pd.DataFrame(l,columns =['Numbers'])


# In[13]:


df


# In[14]:


df.Numbers.dtype  


# #### Convert Float⇒Int

# In[15]:


df['Numbers']=df['Numbers'].astype(int)


# - It rounds all values to down
#     - ie, 4.1→4 , 4.6→4
# - Fix: first round them to nearest whole number
# - df['Numbers'].round(0).astype(int)
#     - round 0 turns 4.1→4, 4.2→4 , 4.6→5
# 
# **or**
# 
# - pd.to_numeric(df['Numbers']) 
#     - gives float ⇒ Downcast to int(but downcast only work if .0 )
#     - So,to get integers
#         1.convert all float values to .0
#         2.Downcast to Integer
# ``` ie,pd.to_numeric(df['Numbers'].round(0),downcast='Integer') ```

# In[16]:


df


# ### Use case 3: Strings + Ints

# In[17]:


# Column mixed with Strings and Ints
l=[1,2,3,'Sahil'] # String + Numbers gets converted to object
df=pd.DataFrame(l,columns =['Numbers'])


# In[18]:


df


# In[19]:


df.Numbers.dtype


# In[20]:


df['Numbers']=pd.to_numeric(df['Numbers'],errors='coerce')
# This errors=coerce converts strings to Nans and keeps the entire row
# But Nan's are floats so our entire column is float now

# This errors=ignore ignores the rows which contains NaNs


# In[21]:


df


# In[22]:


df['Numbers']=df['Numbers'].astype('Int64') 
# It changes numpy's Nan's to pandas <Na> which are ints


# In[23]:


df


# ### Use case 4: Ints + Nans

# In[24]:


import pandas as pd
import numpy as np
l=[1,2,3,np.nan] # even if 1 Nan⇒ nan is considered as float in pandas⇒ entire col gets converted to float
df=pd.DataFrame(l,columns =['Numbers'])


# In[25]:


df


# In[26]:


df.Numbers.dtype


# In[27]:


# Now do the same manipulation as above


# ### Use case 5 : Strings (currencies)

# In[28]:


import pandas as pd
import numpy as np
l=['₹1,5000.00','₹2,500.00','₹3,2000.00'] 
df1=pd.DataFrame(l,columns =['Numbers'])


# In[29]:


df1


# In[30]:


df1.Numbers.dtype


# In[31]:


df1['Numbers']=df1['Numbers'].str.replace('₹','').str.replace(',','').astype(float)


# In[32]:


df1


# In[33]:


df1.dtypes


# In[34]:


df1['Numbers']=df1['Numbers'].astype(int)


# In[35]:


df1

