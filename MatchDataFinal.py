import pandas as pd
import Constant as cnst
"""df = pd.read_excel(open(cnst.MatchedData,'rb'),sheet_name='Feuil1')
df1 =pd.read_excel(open('C:/pikoro/UnMatchedData3.xlsx','rb'),sheet_name='Feuil1')

df= df.append(df1)

with pd.ExcelWriter('C:/pikoro/MatchedDataFinal.xlsx') as writer:
    df.to_excel(writer, sheet_name='Feuil1', index=False)
"""
df = pd.read_excel(open(cnst.upload,'rb'),sheet_name='sheet1')
df = df.to_dict('records')
for i in df :
    x = i['Parcours']
    pos = x.find('(')
    if pos > -1 :
        if x[pos-1] ==' ':
            x = x[:pos-1]

        else:
            x = x[:pos]
    i['Parcours'] = x.title()
df = pd.DataFrame.from_dict(df)
with pd.ExcelWriter(cnst.upload) as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False)
