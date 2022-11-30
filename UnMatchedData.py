import pandas as pd
import numpy as np

df2 = pd.read_excel(open('C:/pikoro/DataManuallyMatched.xlsx','rb'),sheet_name='Feuil1')
ls = df2['Code'].tolist()
ls = np.unique(ls)
df = pd.read_excel(open('C:/pikoro/MatchedDataFinal.xlsx','rb'),sheet_name='Feuil1')
ls2= df['Code'].tolist()
ls2 = np.unique(ls2)
#df = df.loc[df['TyBac']=='Science']
lsfin = pd.DataFrame()
ll= []
for i in ls2 :
    if i not in ls :
        ll.append(i)
print(len(ll))

"""        lsfin =lsfin.append(df.loc[df['Code']==i])
with pd.ExcelWriter('C:/pikoro/UnMatchedDataPrepaMed.xlsx') as writer:
    lsfin.to_excel(writer, sheet_name='Feuil1', index=False)
"""
