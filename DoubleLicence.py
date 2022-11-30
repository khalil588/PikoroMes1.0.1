import pandas as pd
df = pd.read_excel(open('C:/pikoro/MatchedDataFinal.xlsx','rb'),sheet_name='Feuil1')
df1 = pd.read_excel(open('C:/pikoro/DataCoConstruite.xlsx','rb'),sheet_name='Feuil1')
df = df.to_dict('records')
df2 = pd.DataFrame()
l = []
for x in df :
    df3 = df1.loc[df1['Uni']==x['Uni'],['Uni','Camp','CodeP','Type','Domaine','Mention','Parcours','Link']]
    if df3.empty != False :
        df3 = df3.loc[df3['Camp'] == x['Camp'], ['Uni', 'Camp', 'CodeP', 'Type', 'Domaine', 'Mention', 'Parcours', 'Link']]
        if df3.empty != False :
            df3 = df3.loc[df3['Mention'] == x['Mention'], ['Uni', 'Camp', 'CodeP', 'Type', 'Domaine', 'Mention', 'Parcours', 'Link']]
            if df3.empty != False:
                df3 = df3.loc[df3['Parcours'] == x['Parcours'], ['Uni', 'Camp', 'CodeP', 'Type', 'Domaine', 'Mention', 'Parcours','Link']]
                if df3.empty != False :
                    l.append(x)
df2 = pd.DataFrame.from_dict(l)
with pd.ExcelWriter('C:/pikoro/DoubleLicence.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Feuil1', index=False)