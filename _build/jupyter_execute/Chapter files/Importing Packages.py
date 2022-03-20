#!/usr/bin/env python
# coding: utf-8

# ### Importing Packages

# In[1]:


# !import module_name


# Now,all the obects and functions present in that module can be accessed by module name followed by dot(.)
# 
# eg, If lets say module_name has object,s="text" and function,def foo(arg)
# 
# You can access both the things using module_name.s and module_name.foo(5)

# ### Importing everything vs Specifics

# - If you want to import everything: ```import module_name ``` or ```from module_name import *```   
# - If you want to import specific things ```from module_name import s,foo``` 
#     - It will be faster
#     - You can use only things u specified to import

# ### Giving names to Imported modules as shortforms

# In[2]:


# import pandas as pd
# import numpy as np
# import matplotlib as plt

