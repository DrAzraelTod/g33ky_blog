#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,re,codecs
from bs4 import BeautifulSoup
from datetime import datetime

fn = sys.argv[1]

print('converting file: '+fn)

i = open(fn)
o = codecs.open(fn.replace('.old','.html'),'w', 'utf-8')
html = i.read()
i.close()
soup = BeautifulSoup(html)
title = soup.title.text.replace("\n"," ").replace('\\','\\\\').replace('"','\\\"')
title = re.sub('\s+',' ',title)
content = soup.find_all(id='content')[0]
write_date = soup.find_all('p','infos')[0].contents[0].split(u'Geschrieben: ')[-1]
write_date = re.sub('\s+',' ', write_date.replace('\n','')).strip()
write_date = datetime.strptime(write_date,'%d.%b.%Y %H:%M')
o.write('+++\n')
o.write(u'title = "'+title.strip()+'"\n')
o.write(u'date = "'+write_date.isoformat()+'"\n')
author = soup.find_all('span','author')[0].contents[0]
author = author.replace('von ', '').strip()
o.write(u'author = "'+author+'"\n')
tags = soup.find_all('a', title='Andere Artikel mit diesem Tag')
first = True
if len(tags) > 0:
  o.write(u'tags = [')
  for tag in tags:
    if first:
      o.write('"'+tag.text.strip().replace('"','\\\"')+'"')
      first = False
    else:
      o.write(', "'+tag.text.strip()+'"')
  o.write(']\n')
isso = soup.find(id='isso-thread')
issoid = isso.attrs['data-isso-id']
o.write('issoid = "'+issoid+'"\n')
o.write('aliases = "'+issoid+'"\n')
o.write('+++\n')

text = soup.find('div','text')
o.write(text.decode_contents(formatter="html"))

all_old_comments = soup.find('div','comments')
if all_old_comments != None:
  old_comments = all_old_comments.find_all('div','comment', False)
  if len(old_comments) > 0:
    o.write('<div class="old_comments">')
    o.write('<h3>Importierte/Alte Kommentare:</h3>')
    for c in old_comments:
      o.write(c.decode_contents(formatter="html"))
    o.write('</div>')
  
o.close()
