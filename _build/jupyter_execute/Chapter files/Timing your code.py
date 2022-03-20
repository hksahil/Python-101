#!/usr/bin/env python
# coding: utf-8

# ## Timing your Code

# ### Approach 1

# - use time library

# In[1]:


import time
start = time.time()  # tells time in second
"the code you want to test stays here"
end = time.time()
print(end - start)


# ### Approach 2

# use magic command
# - there are some magic commands in jupyter notebook which u can use to measure time
# - '%time'
#     - It is used if you want to measure time of one statement
#     - If using %,write the statement just after you write %time
#         - eg, %time [your statement]
# -'%%time'
#     - It is used if you want to measure time of whole cell
#     - If using %%,don't write anything on same line ie,code should start from next line
#         - eg, %%time
#            
#            [your code]
#     - this can be used for above scenario as well if you write the statement in below line

# ### Examples

# In[2]:


get_ipython().run_line_magic('time', '[i for i in range(1,10,2)]')


# In[3]:


get_ipython().run_cell_magic('time', '', 'l=[i for i in range(1,100000,2)]\nl=l*22')


# In[ ]:




