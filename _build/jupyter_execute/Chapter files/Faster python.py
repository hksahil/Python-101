#!/usr/bin/env python
# coding: utf-8

# ## Faster Python

# - For CPU intensive work
#     - Doing calculations,manipulations etc
#         - Use multiprocessing (not supported in Jupyter)
# - For IO related work
#     - Reading from files/databases/querying large datasets
#         - Use multithreading
# - For basic caching
#     - Use @lru_cache decorator from functools module
#     - With the @lru_cache decorator in place, you store every call and answer in memory to access later if requested again. But how many calls can you save before running out of memory?
# 
#         - Python’s @lru_cache decorator offers a maxsize attribute that defines the maximum number of entries before the cache starts evicting old items. By default, maxsize is set to 128. If you set maxsize to None, then the cache will grow indefinitely, and no entries will be ever evicted. This could become a problem if you’re storing a large number of different calls in memory

# ### Example

# #### Without Caching

# In[1]:


import time
from functools import lru_cache

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


start=time.time()
print([fib(n) for n in range(20)])
end=time.time()
print(end-start)
# with caching,took 0.01s


# #### With Caching

# In[2]:


import time
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


start=time.time()
print([fib(n) for n in range(20)])
end=time.time()
print(end-start)

# with caching,took 0s


# In[ ]:





# In[ ]:




