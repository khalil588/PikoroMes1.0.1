import pandas as pd
import Constant as cnst
from googletrans import Translator
translator = Translator()

df = pd.read_excel(open('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx','rb'),sheet_name='sheet1')
df1 = df.to_dict('records')
for i in df1 :
    y = i['Mention']
    a = str(y)
    if a.find('"') > -1 :
        i['Mention'] = a[:a.find('"')-1]
        print(i['Mention'])
        i['Mention'] = translator.translate(i['Mention'],src="fr",dest="en")
        i['Mention'] = i['Mention'].text
        print(i['Mention'])
df = pd.DataFrame.from_dict(df1)
with pd.ExcelWriter('C:/pikoro/Orientation/Data1.0.1/DataANg/Datang.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False)

