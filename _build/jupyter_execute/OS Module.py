#!/usr/bin/env python
# coding: utf-8

# ## OS Module Basics

# In[1]:


import os


# ### Get current working directory

# In[2]:


os.getcwd() # Most important command


# ### List the files and folders of current directory

# In[3]:


os.listdir()[0:5]


# ### Changing the working directory

# In[4]:


os.chdir('C:\\users\\Sahil Choudhary\\Desktop') # Most important command


# ### List the files and folders of particular directory

# In[5]:


os.listdir("C:\\Users\\Sahil Choudhary\\Documents\\Test folder\\Parent folder")


# In[6]:


os.listdir() #_static
os.chdir("_static")


# In[66]:


os.getcwd()


# ### Making a new directory

# In[67]:


os.mkdir('Test')


# ### OS.walk

# #### Get file names and folder names and the files present in subfolders all in one go

# ![]('https://ibb.co/TvKhBch')

# !['g'](https://i.postimg.cc/x815HRPY/curr.png)

# In[71]:


path='C:\\Users\\Sahil Choudhary\\Documents\\Test folder\\Parent folder'
for root_path,sub_directories,files in os.walk(path):  
    # os.walk(path) gives 3 things
        # parent directory
        # subdirectory
        # files
    print('Parent folder = ',root_path.split('\\')[-1])
    print('Sub directories = ',sub_directories)
    print('Files = ',files)
    print('---------')

