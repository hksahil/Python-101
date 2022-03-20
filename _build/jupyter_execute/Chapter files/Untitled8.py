#!/usr/bin/env python
# coding: utf-8

# In[1]:


from multiprocessing import Pool, cpu_count

def power(p):
    x,n=p
    time.sleep(1)
    return x ** n


def main():
    values = ((2, 2), (4, 3), (5, 5))

    with Pool() as pool:
        res = pool.map(power, values)
        print(res)


if __name__ == '__main__':
    main()


# In[ ]:




