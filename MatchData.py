import Constant as cnst
import pandas as pd
df = pd.read_excel(open(cnst.uploadAng,'rb'),sheet_name='Feuil1')
df1 = pd.read_excel(open('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx','rb'),sheet_name='sheet1')
df1 = df1.to_dict('records')
df = df.loc[df['TyBac']=='Science',['Code','Fil','Uni','Etab','Gouv','Crit','DurEt']]

def unique(x):
    l = []
    for i in x :
        if i not in l :
            l.append(x)
    return l











l = []
m = []
for x in df1 :
    df2 = pd.DataFrame()
    y = x['Uni']
    y = str(y)
    y = y.strip().upper()
    df2 = df.loc[df['Uni'] == y ,['Code','Fil'	,'Uni','Etab','Gouv','Crit','DurEt']]
    if df2.empty == False :
        z = x['Camp']
        z = str(z).strip()
        df2 = df2.loc[df2['Etab'] == z, ['Code', 'Fil', 'Uni', 'Etab', 'Gouv', 'Crit', 'DurEt']]
        if df2.empty == False:
            a = x['Mention']
            a = str(a).strip().upper()
            df2 = df2.loc[df2['Fil'] == a, ['Code', 'Gouv', 'Crit']]
            if df2.empty == False:
                df2 = df2.values.tolist()
                df2 =  df2[0]
                x['Code'] = df2[0]
                x['Gouv'] = df2 [1]
                l.append(x)
            else:
                m.append(x)
print(len(l))
df3 = pd.DataFrame.from_dict(l)
with pd.ExcelWriter(cnst.MatchedData) as writer:
    df3.to_excel(writer, sheet_name='Feuil1', index=False)

"""
l3 = df3['Code'].tolist()
l3 = unique(l3)[0]
l4 = df['Code'].tolist()
l5 = []
for i in l4 :
    v = False
    for j in  l3:
        if i == j :
            v = True
            break
    if v == False :
        l5.append(i)

df6 = pd.DataFrame()
for i in l5 :
    df5 = df.loc[df['Code']==i,['Code','Fil','Uni','Etab','Gouv','Crit','DurEt']]
    if df5.empty == False :
        df6 = df6.append(df5)
print(df6)
with pd.ExcelWriter(cnst.UnMatchedData) as writer:
    df6.to_excel(writer, sheet_name='Feuil1', index=False)
"""




df1 = pd.DataFrame.from_dict(df1)

ls = df1['CodeP'].tolist()
ls2 = df3['CodeP'].tolist()
lf = []

for i in ls :
    v = False
    for j in ls2 :
        if i == j :
            v = True
            break
    if v == False :
        lf.append(i)
print(lf)
l3 = pd.DataFrame()
for i in lf :
    x = df1.loc[df1['CodeP']==i,['Uni','Camp','CodeP','Type','Domaine','Mention','Parcours','Link']]
    l3 = l3.append(x)

with pd.ExcelWriter(cnst.UnMatchedData2) as writer:
    l3.to_excel(writer, sheet_name='Feuil1', index=False)
