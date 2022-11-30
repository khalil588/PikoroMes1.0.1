"""import pandas as pd
df = pd.read_excel(open('C:/pikoro/Orientation/data_Ent/Data.xlsx','rb'),sheet_name='Feuil1')
df2 = pd.read_excel(open('C:/pikoro/dataf/Dataf.xlsx','rb'),sheet_name='Feuil1')
"""
import timeit
import random
loopNum = 100000
def normalFun():
    for _ in range(loopNum):
        random.random()
def optimizedFun():
    nrd = random.random()
    for _ in range(loopNum):
        nrd
print("normal function : ",timeit.timeit(normalFun,number=loopNum))
print("optimized function : ",timeit.timeit(optimizedFun,number=loopNum))

