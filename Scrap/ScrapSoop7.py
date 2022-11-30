import requests
from bs4 import BeautifulSoup
import pandas as pd

def fun(x):
    i = 0
    l = []
    while i > -1 :
        i = x.find('\n')
        l.append(x[:i])
        x = x[i+1:]
    i = 1
    for row in l :
        if row.find('body') > -1 :
           break
        else:
            i+=1
    return l[i+1:-2]






df = pd.read_excel(open('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx','rb'),sheet_name='sheet1')
df = df.to_dict('records')
i = 0
for row in df:
    i+=1
    x = row['CodeP']
    x = x+'_'+str(i)
    print(x)
    link = row['Link']
    r = requests.get(link)
    l = r.text
    n = l.find('<body onload="UR_Start()">')
    l = l [n+26:]
#    print(l)
    l = fun(r.text)

    x = 'C:/pikoro/files/'+x+'.txt'

    with open(x,'w',encoding='utf-8') as f :
#        y = fun(l)
        for row in l:
            f.write("%s \n" % row)
print('done')
