from pathlib import Path
import re

for path in Path('_build/html').rglob('*.html'):
    text = open(path).read()
    if "thebelab" in text:
        text = re.sub("thebelab","thebe",text)
        open(path,'w').write(text)
        print(path,"updated.")




