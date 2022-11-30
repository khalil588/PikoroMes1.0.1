import pandas as pd
df = pd.read_excel(open('C:/pikoro/Orientation/data_Ex/Data.xlsx','rb'),sheet_name='Feuil1')
df = df.to_dict('records')
pd.set_option("display.max.columns", None)
df2 = pd.read_excel(open('C:/pikoro/dataf/DataTronc3.xlsx','rb'),sheet_name='Feuil1')
df3 = pd.DataFrame()
i = 0
for x in df :
    d = df2.loc[df2['Code']== x['Code']]
    if len(d) == 0 :
        print(x)
    d['Crit']= x['Crit']
    d['SDO'] = x['SDO']
    d['DurEt'] = x['DurEt']
    d['TyBac'] = x['TyBac']
    df3 =df3.append(d)
    i+= 1
print(i)
print(len(df3))
with pd.ExcelWriter('C:/pikoro/dataf/DataF.xlsx') as writer:
    df3.to_excel(writer, sheet_name='Feuil1', index=False)


































"""print(len(df))
df2 = pd.read_excel(open('C:/pikoro/dataf/DataTronc2.xlsx','rb'),sheet_name='Feuil1')
df = df.loc[df['TyBac']=='Science']

df2 = df2.to_dict('records')
l = []
for rec in df2 :
    if rec['Code']!= 0 :
       d = df.loc[df['Code']==rec['Code']].values
       if len(d)>0:
           d = d[0]
           rec['Uni'] = d[2]
           rec['Camp'] = d[3]
           l.append(rec)

print(len(l))
df3 = pd.DataFrame.from_dict(l)
with pd.ExcelWriter('C:/pikoro/dataf/DataTronc3.xlsx') as writer:
    df3.to_excel(writer, sheet_name='Feuil1', index=False)
"""