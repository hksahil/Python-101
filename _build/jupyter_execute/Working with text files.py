#!/usr/bin/env python
# coding: utf-8

# ## Working with Text files

# - Text files:
#     - Plain text
#     - XML
#     - JSON
#     - Source code

# - When you open a file,3 modes are there:
#     - Read mode,'r'
#         - If file allready exists,python will read it
#         - If file doesn't exists,python will give error
#             - so wrap it in try block
#     - Write mode,'w'
#         - If file allready exists,python will overwrite it
#         - If file doesn't exists,python will create it
#     - Append mode,'a'
#         - If file allready exists,python will append text in end
#         - If file doesn't exists,python will create it

# ### Read the file

# In[1]:


try:
    with open('sahil.txt','r') as f:
        text=f.read()
    
except FileNotFoundError:
    text=none


# In[2]:


print(text)


# ### Write to file

# In[3]:


l=['A','B','C']
with open('sahil.txt','w') as f:
        for i in l:
            f.write(i)


# #### Check the file

# In[4]:


with open('sahil.txt') as f:
        text=f.read()


# In[5]:


print(text) ### previous text got overwritten
# also,no line separators by default


# #### Adding the new line manually

# In[6]:


l=['A','B','C']
with open('sahil.txt','w') as f:
        for i in l:
            f.write(i)
            f.write('\n')
            


# #### Check the file

# In[7]:


with open('sahil.txt') as f:
        text=f.read()


# In[8]:


print(text)


# ### Append to File

# In[9]:


l=['D','E','F']
with open('sahil.txt','a') as f:
        for i in l:
            f.write(i)
            f.write('\n')
            


# ### Check the file

# In[10]:


with open('sahil.txt','r') as f:
        text=f.read()


# In[11]:


print(text)

