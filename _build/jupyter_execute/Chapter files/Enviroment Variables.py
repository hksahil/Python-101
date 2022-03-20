#!/usr/bin/env python
# coding: utf-8

# ## Enviroment Variables

# - Passwords,API Keys should not be placed in code
# - It should be saved in enviroment variables
# - Replace original passwords by variables and in enviroment variables,set the value of this variable

# In[1]:


db_user='secret_user'
db_password='secret_password'


# ### Setting Enviroment variables

# - Open Control panel>System and Security>System>Advanced system settings>Enviroment variables
# - In user variables>Create new {variable name:variable value}
#     - {secret_user:sahil}
#     - {secret_password:pass}
# - Restart IDE

# ### Accessing the Enviroment variables

# - To access env variables,use os module
# - db_user=os.environ.get('secret_user')
# - db_password=os.environ.get('secret_pass')
#     I
