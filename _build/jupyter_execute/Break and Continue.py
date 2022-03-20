#!/usr/bin/env python
# coding: utf-8

# ## Break and Continue

# - When break is reached,program <b>immediately exits</b> that loop
# - When continue is reached,program jumps to start of that loop
#     - <b>next iteration</b>

# ### Example

# In[1]:


def login():
    while True:
        print('enter name of admin')
        name=input()
        if name!='sahil':
            continue
        print('Hello Admin,enter password')
        password=input()
        if password=='sahil':
            break
    print('Access Granted !!')

