#racp.py

import glob, re

files = glob.glob('./RACCLOG *.txt')

records = []

for file in files:
    fin = open(file, 'r', encoding='utf8')
    lines = fin.readlines()

    record = ''
    matchstr = re.compile(r'\[.*\]')
    for line in lines:
        if matchstr.match(line) is not None:
            records.append(record)
            record = ''
        else:
            record += line
    records.append(record)

print("total " + str(len(records)) + " records.")

cnt=0
for record in records:
    intext = re.sub(r'\<[^>]*\>','\n',record)     # erase <*>
    intext = re.sub(r'\([^)]*\)','\n',intext)     # erase (*)
    intext = re.sub('&lt;','',intext)     # erase &lt;
    intext = re.sub('&gt;','',intext)     # erase &gt;
    intext = re.sub('http://www.gagalive.com','',intext)     # erase &gt;
    for line in intext.split('\n'):
        if '010' in line:     # phone numbers
            cnt+=1
            print(str(cnt) + "(num): " + line)

        eng = re.sub(r'[^a-zA-Z]','',line).strip('\n')
        if eng == '':
            pass
        elif 'SPAM' in line or '스팸' in line:
            pass
        else:                   # ID, URL or email
            cnt+=1
            print(str(cnt) + "(eng): " + line)
