#!/usr/bin/env python
# coding: utf-8

# ## Sort a list

# ### You can use .sort() or sorted() methods

# |  list.Sort() | sorted(list) |
# |---|---|
# | <b>Difference:</b> sorts the list in-place and <b>change the original list</b> & returns None  | takes a list,(or any iterable) ,sort it & <b>returns a new list,sorted </b>  |
# | Works only on lists | Works with any iterable(str,list,dict,tupple) |
# | <b>Syntax:</b> list.sort([key=...], [reverse=True/False)] | new_list=sorted(list, [key=...], [reverse=True/False)]  |
# | <b>Explanation:</b> Since in place so no need to store anywhere and use .  |  Since creates a new list so we need to store it somewhere and org one is passed as args |

# ### Example of using sort()

# In[1]:


a = [3, 2, 1]
print (a.sort()) # in place
print (a)        # it's modified


# ### Example of using sorted()

# In[2]:


a = [3, 2, 1]
print (sorted(a))  # new list,you will need to store it somewhere
print (a)         # is not modified


# ### Keys

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


names=['Sahil','Sonia','Abhi','Sourav']
age=[10,20,30]


# In[4]:


names.sort()
print(names)


# ### What if repeated letters?

# In[5]:


l=['A','B','C','D','A','AA']
l.sort()


# In[6]:


l


# In[ ]:





# In[ ]:





# In[ ]:




