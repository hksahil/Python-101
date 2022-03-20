#!/usr/bin/env python
# coding: utf-8

# ## Any() vs All()

# - any()
#     - Takes iterable
#         - Returns true if any element in iterable is true
#         - Else returns false
# 
# - all()
#     - Takes iterable
#     - Returns true if all the elements in iterable are true
#     - Else returns false

# ### .any()

# In[1]:


all_trues=[True,True,True,1==1]
some_trues_some_falses=[True,False,True,True,False]
all_falses=[False,[],(),{},0]


# In[2]:


print(any(all_trues))
print(all(all_trues))


# In[3]:


print(any(all_falses))
print(all(all_falses))


# In[4]:


# This is where the difference comes

# If you want True if any one of the iterable/condition  is True,like OR conditions,use ANY()
# If you want True if all the iterable/condition are True,like AND conditions,use ALL()

print(any(some_trues_some_falses))
print(all(some_trues_some_falses))


# ### Use cases of any() and all()

# #### Using multiple or conditions
# 
# - if condition1 or condition2 or condition3 or condition4:
#     - do something
#     
# 
# - conditions = (
#     condition1,
#     condition2,
#     condition3,
#     condition4
# )
# - if any(conditions):
#     - Do something here

# #### Using multiple and conditions
# 
# - if condition1 or condition2 or condition3 or condition4:
#     - do something
#     
# 
# - conditions = (
#     condition1,
#     condition2,
#     condition3,
#     condition4
# )
# - if any(conditions):
#     - Do something here

# In[ ]:




