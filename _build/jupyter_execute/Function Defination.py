#!/usr/bin/env python
# coding: utf-8

# ## Function Defination

# - Positional arguments 
#     - by default ones
#         - def foo(a,b)
#         - foo(2,3) # Here a and b are positional arguments and you need to pass both..If u miss even one,error will come
#     - means,the order in which we pass values when we call the function gets assigned its arguments respectively
# - Keyword arguments
#     - you specify it explicitly using = symbol
#         - def foo(a,b='sahil')
#         - foo(2,3) # Here a is positional but b is keyword argument so is optional and you need to pass both..If u miss even one,error will come
#     
# - Note: Keyword arguments should always be in the last during function declaration

# ###  Make any argument as optional

# In[1]:


def hi_random_person(name,age=None):
    print('Hi',name)
    if age:
        print('I am '+ str(age)+' years old')


# In[2]:


hi_random_person('sahil')


# In[3]:


hi_random_person('sourav',24)


# ### Set a default value for a argument

# In[4]:


def hi(name,place='Jammu'):   # note: here name is called positional argument and place is called keyword argument
    print('Hi ' + name+ " from "+ place)


# In[5]:


hi('sahil')


# In[6]:


hi('sourav','Mumbai')


# #### Use case

# In[7]:


# Problem
def add(a,b):
    return a+b

print(add(1,2))
#print(add(1))  # it will throw error

# Solution
def add(a,b=0): # or b=None
    return a+b

print(add(1,2))
print(add(1))  # it will throw error


# ### When you are unsure about the number of arguments - For positional arguments

# - Use single asterick
# - *args
# - Note: it picks all the arguments after the positional arguments are assigned
# - args is tupple by default

# In[8]:


def hi(*arguments): 
    return 'hi'+ str(arguments)


# In[9]:


print(hi('sahil'))
print(hi('sahil','sourav'))


# ### When you are unsure about the number of arguments and you don't want to assign arguments in advance - For keyword arguments

# - Use double asterick
# - **kwargs
# - **kwargs is dictinary by default
# - Note: kwargs (or **) only picks up the = arguments
# - common usecase is when u wrote one function for superclass and in subclasses you need only few arguments

# In[10]:


def hi(**arguments):
    return 'hi'+ str(arguments)


# In[11]:


print(hi('sahil')) # it will give error :hi() takes 0 positional arguments but 1 was given because
# kwargs (or **) only picks the values passed as =


# In[65]:


print(hi(name='sahil'))


# In[67]:


print(hi(name1='sahil',name2='sourav'))


# ### Summary (All used in one Example)

# In[75]:


def hi(a,b,*args,**kwargs):
    return 'hi '+str(a)+ str(b)+ str(args)+ str(kwargs)


# In[76]:


hi(10,20) # both these will be picked by positional arguments (a,b) only 
# also,if you even miss one value and pass only one value,it will throw error.
# all the positional arguments must be passed always.This is the rule


# In[77]:


hi(10,20,30,40) # after taking and b from arguments,rest everything will be taken as args
# and since args comes as tupple by default,they will be in tupple


# In[78]:


hi(10,20,30,40,50,60) # after taking and b from arguments,rest everything will be taken as args
# and since args comes as tupple by default,they will be in tupple
# Note: No kwargs will be taken because nothing is passed as =


# In[80]:


hi(10,20,30,40,50,60,x=70,y=80) # x and y will be taken as kwars since they value =
# and kwargs comes as dictionary by default

