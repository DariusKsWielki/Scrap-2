#!/usr/bin/env python
# coding: utf-8

# In[4]:


from urllib import request
from bs4 import BeautifulSoup as BS

url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
print('Excercise 1.1:')
tags = bs.find_all(lambda tag: (tag.get_text()=='Anna Pavlovna' or tag.get_text()=="Anna Pavlovna's" ) )
print(len(list(tags)))

print('\nExcercise 1.2:')
tags2= bs.find_all(lambda tag: (len(tag.attrs)==1))
for tag in one_at_tags:
    print(tag.name,tag.attrs)
print('\nLength of this list: ',len(tags2))

