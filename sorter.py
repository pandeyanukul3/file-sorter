import os
print("Currently in",os.getcwd())
folder=os.listdir()
extl=[]
for items in folder:
    extl.append(items.split('.'))
extensions=[]
for item in extl:
    for index,i in enumerate(item):
        if index%2!=0:
            if i not in extensions:
                extensions.append(i)
num=1
numDict={}
for itm in extl:
    for index,items in enumerate(itm):
        if index%2!=0:
            if items in extensions:
                if items not in numDict:
                    numDict[f"{items}"]=num
                fval=numDict[f"{items}"]
                if f"{itm[index-1]}.{items}" != "sorter.py":
                 os.rename(f"{itm[index-1]}.{items}",f"Item-{fval}.{items}")
                 numDict[f"{items}"]=numDict[f"{items}"]+1
print('Task executed successfully....')

