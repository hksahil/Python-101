#!/usr/bin/env python
# coding: utf-8

# ## Web Scraping

# - Use beautiful soup library to parse the DOM (It is parser)
# - Use request library to make http requests since inbuild urllib of python is not that good

# In[1]:


get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


with open(https://webscraper.io/) as html_file: # open the file
    #pass the file into soup variable
    soup=BeautifulSoup(html_file,'lxml')
print(soup.prettify())


# # get title tag
# 
# #First title tag on page
# match=soup.title.text
# 
# #First div tag on page
# match=soup.div # it give childs as well
# 
# # Get div of particular class
# # Use find method
# match=soup.find('div',class_='footer')
# 
# # to get all articles no need to use parent div
# for article in soup.find_all('div',class_='footer')
#     article=article.h2.a.text
#     summary=article.p.text
#     print()

# In[ ]:


### Get 1 div with your needs
#article=soup.find('div',class_='article')

# now use dot operators to go inside that article
headline=article.h2.a.text
summary=article.p.text


# In[14]:


# ### Using request library
# source=requests.get('http://coreyms.com').text # html of website
# soup=BeautifulSoup(source,'lxml')

# #Logic->Grab one thing and then use findall and loop to get everything

# article=soup.find('article')
# # Get text
# summary=article.find('div',class_='entry-content').p.text

# # Get attribute (like a dictionary)
# summary=article.find('div',class_='entry-content')['src']
# print(summary)


# In[18]:


### Using request library
source=requests.get('https://usergroups.tableau.com/').text # html of website
soup=BeautifulSoup(source,'lxml')
print(soup.prettify())


# In[ ]:




