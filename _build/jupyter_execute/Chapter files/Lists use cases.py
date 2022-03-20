#!/usr/bin/env python
# coding: utf-8

# ## Lists Use cases

# ### Check if entire list is sublist or not?

# #### Method 1 : using issubset()

# In[1]:


list1=[1,2,3,4,5]
list2=[2,3]

# Logic:
# We allready have issubset() inbuilt function
# And this function only runs on sets
# So first convert lists to subsets


# using issubset()

if(set(list2).issubset(set(list1))):
    print(True)


# #### Method  2 : using all() 

# In[2]:


list1=[1,2,3,4,5]
list2=[6,7,3]

print([x in list1 for x in list2])
all([x in list1 for x in list2])


# ### Check if two lists are same or not

# You can directly use ==

# In[3]:


a=[1,2,3]
b=[1,2,3]

print(a==b)


# #### Problem?
# What happens if lists are unordered?

# In[4]:


a=[1,2,3]
b=[3,2,1]
print(a==b) # !!!!


# #### Solution
# So,we have to first sort the lists and then use the == to compare the lists

# In[5]:


a=[1,2,3]
b=[3,2,1]
print(sorted(a)==sorted(b))

