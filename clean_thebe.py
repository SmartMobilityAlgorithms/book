from pathlib import Path
import re
from bs4 import BeautifulSoup as Soup

for path in Path('_build/html').rglob('*.html'):
    text = open(path).read()
    soup = Soup(text, features='lxml')
    head = soup.find('head')
    if not head:
        continue
    thebe = soup.find(attrs={'src':'https://unpkg.com/thebelab@latest/lib/index.js'})
    if thebe:
        thebe['src'] = re.sub("thebelab","thebe",thebe['src'])
    with open(path,'w') as f:
        f.write(str(soup))
        print(f"{path} updated.")




