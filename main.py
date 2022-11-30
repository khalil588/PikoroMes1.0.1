import  Constant as cnst
import pandas as pd
import time
from Scrap.WebScr import Scrapper2
from Scrap.transform import transform
from googletrans import Translator
translator = Translator()

"""
df = pd.read_excel(open('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx','rb'),sheet_name='sheet1')
df1 = df.to_dict('records')
for i in df1 :
    y = i['Mention']
    a = str(y)

    i['Mention1'] = translator.translate(a,src="fr",dest="en")
    i['Mention1'] = i['Mention1'].text
    print(i['Mention1'])
df = pd.DataFrame.from_dict(df1)
with pd.ExcelWriter('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False)


"""
df = pd.DataFrame()
with Scrapper2(teardown=True) as bot:
    for i in cnst.Univ :
        x = bot.land_first_page(i)
        df = df.append(x)
        print(len(df))

with pd.ExcelWriter(cnst.upload) as writer:
    df.to_excel(writer, sheet_name='sheet1',index=False)

#transform()