import pandas as pd
import numpy as np

df = pd.read_excel(open('C:/pikoro/dataf/DataTronc.xlsx','rb'),sheet_name='Feuil1')
l= df['Code'].tolist()
l = np.unique(l)
"""df2 = pd.read_excel(open('C:/pikoro/Orientation/data_Ex/data.xlsx','rb'),sheet_name='Feuil1')
df2 = df2.loc[df2['TyBac']=='Science']"""
df2= pd.read_excel(open('C:/pikoro/dataf/DataSpec.xlsx','rb'),sheet_name='Feuil1')
print(len(df2))
l2 =df2['Code'].tolist()
l2 = np.unique(l2)
l3 = []
d = pd.DataFrame()
for x in l :
    if x not in l2 :
        l3.append(x)

l4 = []
for i in l :
    if i not in l3 :
        l4.append(i)
        d = d.append(df2.loc[df2['Code']==i])
print(len(l4))
print(len(d))
with pd.ExcelWriter('C:/pikoro/dataf/DataSpec2.xlsx') as writer:
    d.to_excel(writer, sheet_name='Feuil1', index=False)























"""df = pd.read_excel(open('C:/pikoro/MatchedDataFinal.xlsx','rb'),sheet_name='Feuil1')
df2= pd.read_excel(open('C:/pikoro/UnMatchedData3.xlsx','rb'),sheet_name='Feuil1')
df3 = pd.read_excel(open('C:/pikoro/DataManuallyMatched.xlsx','rb'),sheet_name='Feuil1')
print(len(df))
print(len(df2))
print(len(df3))
df4 = pd.DataFrame()
df4 =df4.append(df)
df4 =df4.append(df2)
df4 =df4.append(df3)
print(len(df4))
ls = df4['Code'].tolist()
ls = np.unique(ls)
print(len(ls))
with pd.ExcelWriter('C:/pikoro/Data.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Feuil1', index=False)
"""