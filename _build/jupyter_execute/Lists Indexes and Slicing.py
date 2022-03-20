#!/usr/bin/env python
# coding: utf-8

# ## List Slicing

# In[1]:


names=['Sahil','Sonia','Sourav','Deepak','Vishal']
age=[1,2,3]


# ### Syntax

# - names[starting index:ending index:step]
#     - starting index means where to start from
#         - is inclusive
#         - if omitted,python assumes you want to start from begining
#     - ending index 
#         - is exclusive if specified
#             - if specified,python goes till this index-1
#             - if not specified,python goes till this index(means till end)
#         - if omitted,python assumes you want to go till end
#     - step
#         - Be default 1
#             - 1 means go from left to right (forwards)
#             - -1 means go from right to left (backwards)
#             - 2 or n means steps,skipping
#                 -used to get elements at even/odd positions or every n'th position
#                 
# - <b>INTUITION:</b> Start/End at given position,going from left to right(or opp) and move till start/end/(last/begining if nothing given)

# #### Get Indexes based on element

# In[2]:


names.index('Deepak')


# ### Traversing from left to right

# In[3]:


names[:]
# or names[0:len(names)]
# or [ i for i in names]    
# Note 1:we generally prefer comprehension for iterations of lists
# Note 2:we generally don't use list comprehensions for strings


# ### Traversing from right to left

# In[4]:


names[::-1]
# or [i for i in names[::-1]]


# ### Getting First Element

# In[5]:


names[0]


# ### Getting Second element

# In[6]:


names[1]


# ### Getting first 3 elements

# In[7]:


names[0:3]


# ### Getting last element

# In[8]:


names[-1]


# ### Getting second last element

# In[9]:


names[-2]


# ### Getting last 3 elements

# In[10]:


names[-3:]


# ### Getting Last elements index

# In[11]:


len(names)-1


# ### Give me elements based on index

# In[12]:


# eg,give me sonia,sourav,deepak
names=['Sahil','Sonia','Sourav','Deepak','Vishal']
names[names.index('Sonia'):names.index('Vishal')]  # last index is exclusive so I wrote visal


# ### Give me all even indexes

# In[13]:


names[::2]


# ### Give me all old indexes

# In[14]:


names[::3]


# In[15]:


Give me the nth elements


# In[ ]:


names[::2] # 2 can be replaced by N


# # Summary

# In[ ]:


#   0 1 2 3 4 5 6 7 8  (these are also indexes but positive) positive means from start
a= [1,2,3,4,5,6,7,8,9]
#  -9-8-7-6-5-4-3-2-1  (these are also indexes but negative) negative means from end

# ---

#INTUITION:
# Start/End at given position,going from left to right(or opp) and move till start/end/(last/begining if nothing given)

# ---

# Using positive indexes
a[2] #3
a[2:4] # start from 2,end at 4 and go left to right ,[3,4] since last index is exclusive
a[2:] # start from 2 and go left to right  ,[3,4,5,6,7,8,9]

# Using negative indexes
a[-2] # 8
a[-4:-2] # start from -4,go left to right(because step=1 by default) and end at -2 and  # [6,7]
a[-2:-4] # start from -2,go from left to right(because step=1 by default) and end at -4 and,not possible,so wont give anything
a[-2:] # start from -2,go from left to right(because step=1 by default) #[8,9]
a[:-2] # end at -2 going from left to right, [1, 2, 3, 4, 5, 6, 7],but 8 isn't included since stop index isn't included

# Using steps (means two columns will come into picture)
# if two colons aren't specified,means stepis one means go forward
a[::1] # start from begining, go from left to right ,go till end , [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::-1] # start from ending, go from right to left,go till end, [9, 8, 7, 6, 5, 4, 3, 2, 1]
a[1::-1] # start from 1st index,go from right to left and end at last ,[2, 1]
a[:-3:-1] # end at -3,go from right to left , [9,8]
a[-3::-1] # start at -3,go from right to left , [7, 6, 5, 4, 3, 2, 1]


# In[ ]:




