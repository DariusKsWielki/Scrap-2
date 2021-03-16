#!/usr/bin/env python
# coding: utf-8

# In[4]:


from urllib import request
from bs4 import BeautifulSoup as BS
import re
url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
flags = bs.find_all('img', {'src':re.compile('.+Flag.+')})
for flag in flags:
    print(flag['src'])

