#!/usr/bin/env python
# coding: utf-8

# ## Shallow vs Deep copy

# ### Pre requistic

# ### Difference between == and is 

# - == is used to compare values <b>(are they equal)</b>
# - is is used to compare if same object or not(means pointing to same memory location or not) <b>(are they same)</b>

# In[1]:


# example
a=500
b=500
print(a==b)
print(a is b)

# Note: Python works wierdly in this case if we compare smaller numbers,lets say single digit


# ### Problem?

# In[2]:


a=[1,2,3,4,5]
b=a


# In[3]:


b.pop()


# In[4]:


print(b)
print(a)


# #### Problem is when we created a copy and changed that,old/original one also got changed,ie,it was shallow copy(by default we get shallow copy)

# - Shallow copy- changes on new one affect the old one
# - Deep copy- changes on new one won't affect the old one

# ### Solution

# In[5]:


# use deep copies
import copy
a=[1,2,3,4,5]
b=copy.deepcopy(a)
print(a)
print(b)


# In[6]:


b.pop()


# In[7]:


print(a)
print(b)


# ### All good !!
