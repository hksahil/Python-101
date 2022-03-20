#!/usr/bin/env python
# coding: utf-8

# ## Array Destructuring

# - Destructuring means extracting values at once
# - also called unpacking
#     - unpacking of sequence into item and list

# In[1]:


list=[1,2,3,4,5]


# In[2]:


a,b,c,d,e=list


# In[3]:


print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('e=',e)


# ### Getting last item

# In[4]:


a,*b=list


# In[5]:


print(a)
print(b)


# ### Getting Fist item

# In[6]:


*a,b=list


# In[7]:


print(*a)
print(b)


# ### Getting first,middle and last elements

# In[8]:


head,*mid,tail=list
print(head)
print(*mid)
print(tail)

