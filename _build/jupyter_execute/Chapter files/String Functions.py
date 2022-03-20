#!/usr/bin/env python
# coding: utf-8

# ## String Functions

# | Description  | Function  |
# |---|---|
# | Add leading 0's to str to full the length  | str.zfill(5)   |
# | Convert to upper case  | str.upper()  |
# | Convert to lower case  | str.lower()  |
# | Check if upper case  | str.isupper()   |
# | Check if lower case  | str.islower()  |
# | Check if string is only numbers  | str.isdigit()  |
# | Check if string is only characters  | str.isalpha()  |
# | Check if string is chars+numbers  | str.isalnum()  |
# | Check if string is only spaces and not blank  | str.isspace()  |
# | Remove white spaces from string  | str.strip() (l,r also)   |
# | Remove 0's from left of string  | str.lstrip(0) |
# | Remove 0's from right of string  | str.rstrip(0) |
# | Remove 0's from string  | str.strip(0) |
# | Remove anything from string  | str.strip('abc')  |
# | Replace anything from string  | str.replace('old','new')  |
# | Remove anything from string  | str.strip('abc')  |
# | Check if string starts with abc  | str.startswith('abc')  |
# | Check if string ends with abc  | str.endswith('abc')  |
# | Check if string contains 'abc'  | if 'abc' in str  |
# | Check if string doesn't contains 'abc'  | if 'abc' not in str  |
# | Concatenation or making a string dynamic  | 'Hi {name}'.format(name='Sahil')  |

# ### Note : 
# 
#     - Space is considered as number in python so will be detected in .isnum()
#     - Nan is float in pandas
#     - Left,Right and Mid() functions are not available in python but you can use string slicing to get the same results'
#     - String functions can be chained as well
#         - str.replace().replace()

# ### Example of method chaining

# In[1]:


s='ab123abvba'
s.replace('ab','AB').replace('v','V')


# ### Applying operations on multiple columns

# - Lets say you want to convert datatype of multiple columns
# 
# 
# - Format to convert datatype of one column
#     - ```df['col'].astype(int)```
#     
#     
# - Format to convert datatype of multiple columns
#     - Store the list of col names in list
#         - ```list=['A','B','C']```
#         
#     - Iterate through the list and do the operation on single single element of iterable
#         - ```for i in list:
#             df[i].astype(int)```
