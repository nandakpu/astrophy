import csv
import pandas as pd

data1 = pd.read_csv("file1.csv",sep='\s+')

def Merge(dict1,dict2):
    # res=dict1|dict2
    dict1.update(dict2)
    # return res
    return dict1
data2 = pd.read_csv("file2.csv",sep='\s+')

k=0
new=pd.DataFrame()
for i in range(len(data1)):
    # print(data1.loc[i, "RA"], data1.loc[i, "Dec"])
    RA1=data1.loc[i, "RA"]
    Dec1=data1.loc[i,"Dec"]
    for j in range(len(data2)):
        RA2=data2.loc[j,"RAs"]
        Dec2=data2.loc[j,"Decs"]
        # print(i," ",j)
        if (RA2-RA1 < 0.00067) and (Dec2-Dec1 <0.00067):
            d1=data1.loc[i].to_dict()
            d2=data2.loc[j].to_dict()
            # res=pd.concat([d1,d2],axis=1,join='inner')
            res=Merge(d1,d2)
            new=new.append(pd.DataFrame(res,index=[k]))
            print(new)
            k=k+1
            #if k==100:
               # break
    #if k==100:
            #break
new.to_csv('file3.csv',sep="\t")     
    
# if (RA2-RA1)**2 cos