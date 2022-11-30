import Constant as cnst
import pandas as pd

def transform ():
    df =  pd.read_excel(open(cnst.uploadAng,'rb'),sheet_name='Feuil1')
    d = df.to_dict('records')
    l = []
    for row in d :
        x = row['Fil']
        y = x[:4]
        y = y.upper()
        if x[:5] == 'L. EN':
            row['Fil'] = x[6::]
            print(row['Fil'])
            l.append(row)
        elif x[:4] == 'L EN':
            row['Fil'] = x[5::]
            l.append(row)
            print(row['Fil'])
        elif x[:4].upper() == 'LICE':
            row['Fil'] = x[8::]
            print(row['Fil'])
            l.append(row)
        elif x[:2].upper() =='EN':
            row['Fil'] = x[3:]
            print(row['Fil'])
            l.append(row)
        else:
            l.append(row)

    return l
df1 = pd.DataFrame.from_dict(transform())

with pd.ExcelWriter(cnst.uploadAng) as writer:
    df1.to_excel(writer, sheet_name='Feuil1', index=False)

