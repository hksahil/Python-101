#!/usr/bin/env python
# coding: utf-8

# ## Counter

# In[1]:


from collections import Counter


# ### Logic

# - Counter(pass any iterable here)
#     - It will give dictionary of keys(elements) and values(count)
#         - Accessing the count:
#             - Since it returns dict,you can use counter.keys(),counter.values() and counter.items()
#             - or if you want count of specific key,you can do counter()['that key']

# ### Example

# In[2]:


l=[1,2,3,3,4,5,5,5,5,5,5,5,5,5,5]


# In[3]:


print(Counter(l).keys())
print(Counter(l).values())
print(Counter(l).items())


# ### Counting in lists

# In[4]:


l=[1,2,3,3,4,5,5,5,5,5,5,5,5,5,5]
Counter(l)


# ### Counting in String

# In[5]:


s='sahilsahil'
Counter(s)


# ### Counting in dictionary

# In[6]:


d={
    'a':10,
    'b':20,
    'c':40
}


# In[7]:


Counter(d)


# ### Getting count of specific element

# In[8]:


Counter(d)['c']


# ### Extra Functions we can use on Counter object

# In[9]:


l=[1,2,2,3,4,4,5,6,6,6,6,6]
print(Counter(l).most_common(1)) # highest occurence(count)
print(Counter(l).most_common(2)) # top 2 based on occurence(count)


# ### More

# - Since it gives dict object,we can use all the dict operations and perform conditions and everything

# In[10]:


[k for k,v in Counter(l).items() if v==5]

