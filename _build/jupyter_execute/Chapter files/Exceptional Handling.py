#!/usr/bin/env python
# coding: utf-8

# ## Exceptional Handling

# - In Python:
#     - Syntax errors or system errors(like out of memory)=Errors
#     - Logical erors=Exceptions
#     - Exceptions are triggered when error occurs
#     - We can handle these errors to avoid program to avoid

# #### Python's Exceptions List

# | Name  | Description   |
# |---|---|
# | Name error  | If non existing variable is tried to be accessed  |
# | Value error  | If wrong value is passed in parameters ,eg sqrt(-5)   |
# | Type error  | If wrong data type is used |
# | Key error  | If non existing key is requested from dictionary  |
# | Attribute error  | If .property doesn't exist,eg obj.foo and foo doesn't exist  |
# | Index error  | If index out of datatype is tried to be accessed  |

# ### Handling the exceptions to avoid flow/execution of code

# try,catch ===> try except

# In[1]:


# value=a/b
# This code can give errors if users gives 0 as b


# ![alt text for screen readers](https://res.cloudinary.com/dyd911kmh/image/upload/v1633675298/python-try-except-else-finally_doblhm.png)

# In[2]:


try:  # always
    value=a/b
    print(value)
except ZeroDivisionError:  # if error
    print('Division error')
except:
    print('Any other generic exception')
else:  # If no error
    print('No error')

