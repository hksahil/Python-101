#!/usr/bin/env python
# coding: utf-8

# ## Working with Text files

# - Pypi is like npm
# - you can upload your own libraries here and others can install using pip

# ### Setting up your own package

# In[1]:


- create new folder
    - create new folder
        - setup.py code
        - readme.txt
        - license.txt
    - config.txt
    - __main__.py ->
    - __init__.py -> root of package->keep the version here 
    - feed.py -> code file
    - viewer.py -> code file


# In[ ]:





# In[ ]:


###


# In[ ]:


from setuptools import setup,find_package
setup(name="packagesahil",
     vesion="0.1",
     description="This is code with Sahil",
     long_description="long description",
     author="",
     packages=['packagesahil'],
     install_requires=[])


# In[ ]:




