import pandas as pd
import Constant as cnst
#from Translator import Trans

def transform():
    df = pd.read_excel(open(cnst.upload,'rb'),sheet_name='sheet1')
    df1 = df.to_dict('records')
    for i in df1 :
        y = i['Mention']
        a = str(y)
        if a.find('"') > -1 :
            i['Mention'] = a[:a.find('"')-1]
    df = pd.DataFrame.from_dict(df1)
    with pd.ExcelWriter(cnst.upload) as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)

"""def trad() :
    df = pd.read_excel(open(cnst.upload,'rb'),sheet_name='sheet3')
    df1 = df.to_dict('records')
    for row in df1 :
        row['Uni'] = Trans(row['Uni'] )
        row ['Camp'] = Trans(row ['Camp'])
    df = pd.DataFrame.from_dict(df1)
    with pd.ExcelWriter('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
"""



transform()