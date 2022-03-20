#!/usr/bin/env python
# coding: utf-8

# ## Dictionary Advance concepts

# ### Problems with dict

# In[1]:


dict1={
    'a':10,
    'b':20,
    'c':30,
    'd':40,
    'e':50
}


# In[2]:


dict1['a']


# In[3]:


dict1['f']

# It throws an error


# ### Solution

# - dict.get
# - defaultdict - sets its default for the entire dict 
# - dict.setdefault() - sets its default per element

# #### Why to use dict.get() instead of dict[key]

# - If you use dict[key],it is prone to errors if that key isn't present in dictionary as we saw above
# - So you can use dict.get(),it won't give error even if key isn't present.
#    - It will just say None if you haven't specified anything
#    - It will return the value if you have specified anything
# - dict.setdefault is like dict.get, but it'll <b>set given default value to the key</b> if it doesn't already exist
#     - It is not very famous,default dict is more used
# - defaultdict will automatically populate every key with a default value
# 
# 
# - <b>defaultdict vs setdefault:</b>
#     - both sets the default vales for keys if those keys don't exist in order to avoid getting errors
#     - The difference is:
#         - dict.setdefault() - sets its default per element
#         - defaultdict - sets its default for the entire dict 

# ### dict.get()

# #### Syntax 

# dict1.get(key[, default_value])

# In[35]:


dict1={
    'a':10,
    'b':20
}
print(dict1.get('a'))
print(dict1.get('f'))
print(dict1.get('f','f is not present'))


# ### dict.setdefault()

# ### Syntax

# dict.setdefault(key[, default_value])
# - returns:
#     - value of the key if it is in the dictionary
#     - None if the key is not in the dictionary and default_value is not specified
#     - default_value if key is not in the dictionary and default_value is specified

# #### When key is present in the dictionary

# In[42]:


dict1={
    'a':10,
    'b':20
}
print(dict1.setdefault('a')) #not a usecase
print(dict1)


# #### When key is not present in the dictionary

# - when value isn't passed

# In[43]:


print(dict1.setdefault('g'))
print(dict1)


# - when value is passed

# In[44]:


print(dict1.setdefault('g','30'))  #actual usecase
print(dict1)


# ### defaultdict

# - Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. 
# - The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet). 
# 
# 
# - defaultdict is a datatype( not present in default python,needs importing) like dict with Default Values where you’ll never get a KeyError

# In[53]:


# importing defaultdict from collections
from collections import defaultdict

# initializing them
dict1 = defaultdict(lambda: 1) # setting custom defalt value manually

# defaultdict(int)   # As int has been passed as default, any unknown key will return 0 by default
# defaultdict(float) # The Default Value is "0.0"
# defaultdict(str)   # The Default Value is ""

dict1['a']=10
dict1['b']=20
print(dict1)
print(dict1['b'])
print(dict1['c'])
print(dict1)


# ### Use case of list in defaultdict

# - In dictionaries,keys are unique,means only one key with same name can exist
# - Even if you try to add two keys of same name,previous one will be removed automatically
# - So if you want that two keys of same name can exist and if they do,append those in list,we can use this below logic

# In[100]:


dict1 = defaultdict(list)
d=[('a',10),('b',20),('a',30)]


# In[103]:


for i,j in d:
    dict1[i].append(j)


# In[102]:


dict1

