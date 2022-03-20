#!/usr/bin/env python
# coding: utf-8

# ## SQL vs Pandas

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame({
'Name':['Sahil','Sonia','Sourav','Vishal'],
'Age':[10,20,30,40],
'Gender':['M','F','M','M'],
'City':['J','K','L','P'],
'Work':[True,False,False,True]
}
)
df


# ### SQL vs Pandas - Basics

# - Select * from Table
#     - ```df```
#     
#     
# - Select **name** from Table
#     - ```df['name'] or df[['name']]```
#     
#     
# - Select **name,age** from Table
#     - ``` df[['name,'age']]```
#     
#     
# - Select * from Table **limit** 7
#     - ```df.head(7)```
#     
#     
# - Select **distinct** name from table
#     - ``` df['name'].unique() ```
# 
# 
# - Select * from Table **where** name='sahil'
#     - ``` df[df['name']=='sahil']```
#     - ``` df[df.name=='sahil']```
#     
#     
# - Select name from Table where name='sahil'
#     - ``` df[df['name']=='sahil']['name']```
#     
#  
# - Select name,age from Table where name='sahil'
#     - ``` df[df['name']=='sahil'][['name','age]]``` # double quotes in end
#     
#     
# - Select * from Table where name='sahil' **and** age=30
#     - ``` df[(df['name']=='sahil') & (df['age']==30) ]``` # end won't work
#     
#     
# - Select * from Table **sort** by age
#     - ``` df.sort_values(by='age',ascending=False)```
#     
#     
# - Select name,count(*) from table group name
#     - df.groupby('name').count()
#     - df[['name','age]].groupby('name').count()

# ### SQL vs Pandas - Advance

# - SQL : ```SELECT sum(total_bill) FROM tips```
# - Pandas : ```pd.Series(tips['total_bill'].sum())```

# - SQL : ```SELECT sum(total_bill) FROM tips where tip > 5```
# - Pandas : ```pd.Series(tips[tips['tip'] > 5]['total_bill'].sum())```

# - SQL : ```SELECT sum(total_bill) FROM tips where tip > 5 and size > 1```
# - Pandas : ```pd.Series(tips[(tips['tip'] > 5) & (tips['size'] > 1)]['total_bill'].sum())```

# - SQL : 
# 
# ```SELECT 
# sum(total_bill),
# avg(size),
# min(tip),
# FROM 
# tips 
# where tip > 5
# Group by sex,day
# Order by total_bill desc,tip asc```

# - Pandas : 
# 
# ```tips[tips['tip'] > 5]
# .groupby(['sex', 'day'])
# .agg({'total_bill': ['sum'], 'size': ['mean'], 'tip': ['min']})
# .sort_values(['total_bill', 'tip'], ascending = [False, True])```

# In[ ]:




