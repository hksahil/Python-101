#!/usr/bin/env python
# coding: utf-8

# ## Regex Examples

# ### Example 1

# In[1]:


# joo select
# koo select
# loo select
# woo
# moo select
# zoo
# coo


# - Step 1: Write all the results separately you need

# joo
# 
# koo
# 
# loo
# 
# moo

# - Step 2:Create imaginary line and separate them to find a pattern
#     - Usually we start creating lines whereever the similar pattern (like it happened with http and https) is breaking and then in end try to replicate each section by regex
#     (see the last example for refernce)

# j|oo
# 
# k|oo
# 
# l|oo
# 
# m|oo

# - Step 3: Write the expression

# - Pattern : [j-m]oo

# ### Example 2

# In[2]:


# xxx.yy select

# xx.yyyy select

# x.yy select

# xy

# xxyy

# yyxx

# yx

# yxxx


# xxx|.|yy
# 
# xx|.|yyyy
# 
# x|.|yy

# - Pattern : x*\.\y*

# ### Example 3

# In[3]:


# foobarbaz # select
# foobazbcr # select
# baazfobfd


# foo|bar|baz
# 
# foo|baz|bcr

# - 
# Pattern : ^foo*

# ### Example 4

# foo|aaa|bar
# 
# foo|a|bar
# 
# foo|aa|bar

# - Pattern : fooa+bar # ^foo can also be used

# ### Example 5

# http|s|:|//website
#     
# http|:|//website

# - Pattern : https?://website
