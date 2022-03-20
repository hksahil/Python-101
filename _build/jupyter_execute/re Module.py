#!/usr/bin/env python
# coding: utf-8

# ## re Module

#     - Regex is useful if the field you want to play with has no standardised pattern,it is mixed with some non patterns as well and you want to extract your specified pattern. If the pattern in entire column is same,then instead of regex,string functions like split,replace,find can also be used
#         - eg,if names=[Mr Sahil,Mrs XYZ,Mr Sourav],then you do not need regex,directly split it by space and take the second word but if names=[Mr Sahil,Mrs XYZ,abc,Mr Sourav,hello world,1233] then you will need regex
#     - All the patterns which we create are case sensitive
#     - Create a pattern using re.compile(r"\d")
#     - Run this pattern on your string using methods like pattern.finditer(string) to get the matches
#     - Matches is a iterable object

# In[1]:


import re


# In[2]:


s='123abc323abc23ABC'


# In[3]:


pattern=re.compile(r"abc") 
# r means it is a raw string,treat is as string,even if special chars like \n \t are there


# - Arguments for re.compile:
#     - re.IGNORECASE

# ### Raw strings

# - To escape some reserved characters(patterns like \t) from python and treat them just as simple strings,append r in front of string

# In[4]:


a="\t\nHello"
print(a)


# In[5]:


a=r"\t\nHello"
print(a)


# ### Escaping characters from regex

# - . has a special meaning in regex
#     - It is not just a simple string,it is used to tell regex that . means match all the pattern
# - So,if you want that it should be treated normally as string,not as regex character,escape it.
# - Use Backslash to *escape it from regex*
#     

# ### Methods we can apply on pattern

# - ``` .match() ```
#     - scans the text for your mentioned pattern and check if the pattern you are looking for, **is in the begining of string or not**
#         - if its in the begining,it will return that match
#         - if its not,it will return None
#         
#         
# - ``` .search() ``` 
#     - scans the text for your mentioned pattern and **returns first match** if found else return None
#     
#     
# - ``` .findall() ```
#     - scans the text for your mentioned pattern and **return all the matches**
#     
#     
# - ```.finditer()```
#     - scans the text for your mentioned pattern and **return all the matches + their locations**
#     
#     
# 
# - Modify:
#     - sub()
#         - re.sub("regular expression's output",string you want re's ouput to be replaced with,string where search is to be made")
#         - replaces all the matches with specified string

# In[6]:


matches=pattern.finditer(s)


# In[7]:


for match in matches:
    print(match)


# ### Methods we can apply on match object

# - ```match.span()``` - returns a tupple of locations(start,end) of matches
# - ```match.start()``` - returns the starting location of matches
# - ```match.end()``` - returns the ending location of matches
# - ```match.group()``` 
#     - If 0 is passed in arg,will return the entire match
#     - If 1 is passed in arg,will return the first group[() is a group)
#     - If 2 is passed in arg,will return the second group[() is a group)

# ### Examples

# In[8]:


s='1abc3abc_ABC'


# In[9]:


pattern=re.compile(r".") # . means any character
matches=pattern.finditer(s)


# In[10]:


for match in matches:
    print(match.group())


# In[11]:


s='1abc3ab.cABC'
pattern=re.compile(r"\.") # if you want the dot # !!
matches=pattern.finditer(s)


# In[12]:


for match in matches:
    print(match.group())


# In[13]:


# Remove numbers

s='1abc3a_123b.cABC'
pattern=re.compile(r"\D") # if you want the dot # !!
matches=pattern.finditer(s)

for match in matches:
    print(match.group())


# In[14]:


# Remove everything except Numbers

s='1abc3a_123b.cABC' # !!
pattern=re.compile(r"\d") # if you want the dot
matches=pattern.finditer(s)

for match in matches:
    print(match.group())


# In[15]:


# Remove Spaces

s='1abc3a_1  23b.cAB   C' # !!
pattern=re.compile(r"\S") # if you want the dot
matches=pattern.finditer(s)

for match in matches:
    print(match.group())


# In[16]:


dates="""
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-05-02
2020-06-19
2020-08-02
2020_04_04
2020_04_04
hello
no date
123
2020/08/02
2021/09/03

"""


# In[17]:


# Extract dates with yyyy-mm-dd format
# Note: \d means number
pattern=re.compile(r"\d\d\d\d-\d\d-\d\d") # !!
# or pattern=re.compile(r"\d{4}-\d{2}-\d{2}")
matches=pattern.finditer(dates)
for match in matches:
    print(match)


# In[18]:


# Extract dates with yyyy/mm/dd format
# Note: to get / , we have to escape it using backslash=> \/
pattern=re.compile(r"\d\d\d\d\/\d\d\/\d\d") # !!
matches=pattern.finditer(dates)
for match in matches:
    print(match)


# In[19]:


# Extract dates with either yyyy-mm-dd format or yyyy/mm/dd format 
# Note: Here because we need or(among two chars,we are using set[])
pattern=re.compile(r"\d\d\d\d[-/]\d\d[-/]\d\d") # !!
matches=pattern.finditer(dates)
for match in matches:
    print(match)


# In[20]:


# Extract only dates which falls in May or June
# Note: Her because we need or(among two chars,we are using set[])
pattern=re.compile(r"\d\d\d\d[-/]0[5-6][-/]\d\d") # !!
matches=pattern.finditer(dates)
for match in matches:
    print(match)


# In[21]:


# Extract dates with any format
# Note:. Means anything,any character can be there
pattern=re.compile(r"\d\d\d\d.\d\d.\d\d") # !!
matches=pattern.finditer(dates)
for match in matches:
    print(match)


# In[22]:


names="""
Mr Sahil
Mr. Sahil
Ms Smith
hello world
123
2020-05-20
Mr. XYZ

"""


# In[23]:


# Extract all the Misters
# Note:. is optional Sometimes there,sometimes not characters can 
# w denotes letter + means of any length
pattern=re.compile(r"Mr\.?\s\w+") # !!
matches=pattern.finditer(names)
for match in matches:
    print(match)


# In[24]:


# Extract all the Mrs,Mrs,Ms
# Note: We need grouping.grouping is done using (grp1|grp2)
pattern=re.compile(r"(Mr|Ms|Mrs)\.?\s?\w+") # !!
matches=pattern.finditer(names)
for match in matches:
    print(match)


# In[25]:


emails="""
sahil
choudhary
helloworld
1233
sahil@gmail.com
sahil1@yahoo.com
python-ds@reddif.org
py-2313en@ee.com
"""


# In[26]:


pattern=re.compile(r"[a-zA-Z0-9-]+@") # !!
matches=pattern.finditer(emails)
for match in matches:
    print(match)


# In[27]:


pattern=re.compile(r"[a-zA-Z0-9-]+@[a-zA-Z]") # !!
matches=pattern.finditer(emails)
for match in matches:
    print(match)


# In[28]:


pattern=re.compile(r"[a-zA-Z0-9-]+@[a-zA-Z]+") # !!
matches=pattern.finditer(emails)
for match in matches:
    print(match)


# In[29]:


pattern=re.compile(r"[a-zA-Z0-9-]+@[a-zA-Z]+\.[a-zA-Z]") # !!
matches=pattern.finditer(emails)
for match in matches:
    print(match)


# In[30]:


pattern=re.compile(r"[a-zA-Z0-9-]+@[a-zA-Z]+\.[a-zA-Z]+") # !!
matches=pattern.finditer(emails)
for match in matches:
    print(match)


# #### Note: if you want in the future that you will need to fetch username,domain name and server suffix as separate,do the grouping
#     - Take your normal pattern and wrap each section in (),these will become groups
#     - Then,you can refer entire match normally like before if you just write match.group()
#     - And,if you need usernames,write(match.group(1))
#     - And,if you need domain names,write(match.group(2))
#     - And,if you need server suffix,write(match.group(3))

# In[31]:


# Took the normal pattern and wrapped it in ()
pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches=pattern.finditer(emails)
for match in matches:
    print(match)   # !!


# In[32]:


pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches=pattern.finditer(emails)
for match in matches:
    print(match.group())   # !!


# In[33]:


pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches=pattern.finditer(emails)
for match in matches:
    print(match.group(0))   # !!
# group(0)==group()==normal match


# In[34]:


pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches=pattern.finditer(emails)
for match in matches:
    print(match.group(1))   # !!
# group(1)==group1 in our match


# In[35]:


pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches=pattern.finditer(emails)
for match in matches:
    print(match.group(2))   # !!


# In[36]:


pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches=pattern.finditer(emails)
for match in matches:
    print(match.group(3))   # !!


# In[37]:


pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
new_str=pattern.sub("hello",urls)


# ### Uses of group()in re

# In[42]:


string="I am 12abc I ma 9 an 19"
matches=re.finditer('(\d+)',string)
 # Get the first number
for match in matches:
    print(match.group(1))  
  


# ### Uses of re.sub

# In[31]:


string="US,U.S is abc 78 shds USA"


# In[32]:


re.sub('US|U.S|USA',"america",string)


# In[51]:


# Renove # comments

string="12-21-12# commentssss"
#any character after the hash=> # . *
new_string=re.sub(r'#.*',"",string)
print(new_string)


# In[50]:


# Remove -

string="12-21-12 # commentssss"
# Replace non digits with none
re.sub(r'\D',"",string)


# ### Combining of group and sub

# - If in strings ,there are three numbers and you want to replace the third one,
#     1. group the results
#     2. get the third group
#     3. run re.sub on that
