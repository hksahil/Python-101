#!/usr/bin/env python
# coding: utf-8

# ## Playing with Missing values in dataframe

# ### Step 1: Detect the missing values

# ``` missing_values=["N/A","na",np.nan(which is NaN)] ```

# - By default, pandas only consider NaN as missing
# - It ignores na and N/a⇒ Specify custom Nan's while loading file
# - pd.read_csv('',na_values=missing_values) # very useful

# *Note: If you want to create missing values(NaN)-> use np.nan*

# ### Step 2: Find the number of missing values in each column

# ``` df.isnull.sum() ``` 
# - will give colname → total missing values in that column

# ```sns.heatmap(df.isnull(),yticklabels=False,annot=True) ```
# - will plot the missing values

# ### Step 3: Handle the Missing Values

# - **Remove** the nan's
#     - df.dropna() is used
#     - **Remove the rows containing NaNs**
#         - Atleast one NaN is there
#             - ```df.dropna(inplace=True)``` ( is similar to df.dropna(axis=0,how='any',inplace=True))
#             
#         - When all values are NaN
#             - ```df.dropna(axis=0, how='all',inplace=True)```
#         
#         - If NaNs>certain threshhold
#             - ```df.dropna(axis=0, thresh=2,inplace=True)```
#             
#         - if NaNs only in specific columns
#             - ```df.dropna(subset=['ID'],inplace=True)```
#         
#         - **Remove the columns containing NaNs**
#             - Atleast one NaN is there
#                 - ```df.dropna(axis=1,inplace=True)```
#                 
#             - When all values are NaN
#                 - ```df.dropna(axis=1, how='all', inplace=True)```
#             
#             - If NaNs>certain threshhold
#                 - ```df.dropna(axis=1, thresh=2, inplace=True)```
#     
#     
# - **Replacing** the NaN's (missing values) by something else
#     - df.fillna() is used
#     - Note: If you have to replace NaNs on entire df,use df.fillna() but if you want to replace NaNs or any particular column,use df['name'].fillna()
#         - Replace with 0
#             - ```df.fillna(0,inplace=True)```
#         - Replace with anything else
#             - ```df.fillna("any value",inplace=True)```
#         - Other methods
#             - Above cell's value will be copied in NaN
#                 - ```df.fillna(method="ffill",inplace=True)```
#             - Below cell's value will be copied in NaN
#                 - ```df.fillna(method="bfill",inplace=True)```
#             - Take the average of above and bottom value of NaN's (above+below/2)
#                 - ```df.interpolate()```

# In[ ]:




