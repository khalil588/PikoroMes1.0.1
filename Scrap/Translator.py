from googletrans import Translator
translator = Translator()
import  Constant as cnst
import pandas as pd
pd.set_option("display.max.columns" ,None)

def Trans(x):
    t = translator.translate(x,src="fr",dest="en")
    print(t.text)
    return t.text
#Higher School of Digital Economy of Manouba

df = pd.read_excel(open(cnst.upload,'rb'),sheet_name='sheet1')
df1 = pd.read_excel(open('C:/pikoro/MatchedDataFinal.xlsx','rb'),sheet_name='Feuil1')
df1 = df1.to_dict('records')
df2 = []
for i in df1:
    x = i['CodeP']
    l = df.loc[df['CodeP']==x,['Uni','Camp']]
    l = l.to_dict('records')
    l = l[0]
    i['Uni'] = l['Uni']
    i['Camp'] = l['Camp']
    df2.append(i)

df2 = pd.DataFrame.from_dict(df2)
print(df2)
with pd.ExcelWriter('C:/pikoro/MatchedDataFinal.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Feuil1', index=False)
































#Translate to english
"""def openSheet():
    df = pd.read_excel(open(cnst.uploadAng,'rb'),sheet_name='Feuil1')
    return df

def TradData():
    df = openSheet()
    d = df.to_dict('records')
    for row in d :
#        row['Uni'] = Trans(row['Uni'])
        row['Fil1'] = Trans(row['Fil']).upper()
    df1 = pd.DataFrame.from_dict(d)
    with pd.ExcelWriter(cnst.uploadAng) as writer:
        df1.to_excel(writer, sheet_name='Feuil1', index=False)
TradData()

"""


