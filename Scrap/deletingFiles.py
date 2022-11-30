import os
import glob
ls = glob.glob('C:/pikoro/files/*.txt')
ls2= []
for row in ls :
    x = row
    sz = os.path.getsize(row)
    if sz < 10240 :
        ls2.append(row)
        os.remove(row)
        print(f'the {row} has been deleted!!')

print(ls2)
print(len(ls2))