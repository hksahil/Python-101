#!/usr/bin/env python
# coding: utf-8

# ### Pathlib Module

# - Module to use same path for different OS's

# ### Older ways

# - defining paths manually
#     - data_folder = "source_data\\text_files\\"
#     - file_to_open = data_folder + "raw_data.txt"
#     - f = open(file_to_open)
# - using os.path module
#     - data_folder = "source_data\\text_files\\"
#     - file_to_open = data_folder + "raw_data.txt"
#     - f = open(file_to_open)

# ### Pathlib

# - Check easily if file exists
# - To deal with file extensions
# - Common operations with paths
# - Inbuilt in python 3.4 ,so no need to install
# - treat paths as obects

# In[1]:


from pathlib import Path
import os


# In[2]:


Path() # If no arguments passed,Current folder
# relative path to the current folder


# In[3]:


Path('_build/subfolder')


# ### Creating a path by passing folder and file name

# In[4]:


Path("_build/subfolder", "file1.json")


# ### Get home directory

# In[5]:


home_dir=Path.home() # In windows,home directory is C:/Users:/Username
home_dir


# ### Get Current working directory

# In[6]:


cwd=Path.cwd()
print(str(cwd))


# ### Change current working directory

# In[7]:


os.chdir('C:\\users\\Sahil Choudhary\\Desktop') # Most important command


# ### Get the parent directories

# In[8]:


# Get the first parent
one_above=Path.cwd().parent
print(one_above)

n_above=Path.cwd().parents[0]
n1_above=Path.cwd().parents[1]
print(n_above)
print(n1_above)


# ### Joining paths

# In[9]:


joined_path=cwd/'Output'
# joined_path=cwd/'Output'/'Subfolder'
joined_path


# ### Create folder if not exists

# In[10]:


Path.cwd().mkdir(exist_ok=True)


# ### Get file name with extension

# In[11]:


example_file=cwd/'Python 101.ipynb'


# In[12]:


example_file.name


# ### Check if file exists

# In[13]:


example_file.is_file()


# ### Get file name without extension

# In[14]:


example_file.stem


# ### Get only the extensions

# In[15]:


example_file.suffix


# ### Iterate over all the files in directory

# In[16]:


folder=cwd/"_build/subfolder"
for file in folder.iterdir():
    print(file)


# ### Iterate over specific file types

# In[33]:


for file in folder.iterdir():
    if file.suffix=='.html':
        print(file)


# ### Iterate over files inclusive of subdirectories

# In[34]:


for file in folder.rglob("*"):
    print(file)


# ### Summary

# In[63]:


from pathlib import Path # Now,we have path function which has certain important attributes


# In[64]:


Path.cwd()


# In[74]:


# OLD METHODS TO DEFINE PATHS

# path1="C:\Users\Sahil Choudhary\Book\Python\_build\subfolder"  # This will give error
path2=r"C:\Users\Sahil Choudhary\Book\Python\_build\subfolder" # r means raw string.Should be added before paths
path3="C:\\Users\\Sahil Choudhary\\Book\\Python\\_build\\subfolder" # works in windows 
path4="_build\subfolder" # relative path
path5="_build\\subfolder" # relative path 


# In[ ]:


C:\Users\Sahil Choudhary


# In[72]:


# NEW METHOD TO DEFINE PATHS
path6=Path('_build/subfolder') # relative path in pathlib


# In[70]:


for file in path6.iterdir():
    print(file)


# In[ ]:




