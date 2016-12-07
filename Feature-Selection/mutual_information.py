import sys
import math

### read data
f=open(sys.argv[1]);

data=[];
i=0;
l=f.readline();
while(l!=''):
    a=l.split();
    l2=[];
    for j in range(0, len(a)):
        l2.append(int(a[j]));
    data.append(l2);
    l=f.readline();
    i+=1;
    print("read ",i);
nd=len(data);
m=len(data[0]);

### read train labels
f=open(sys.argv[2]);
label=[-1]*nd;
l=f.readline();
n=0;
while(l!=''):
    a=l.split();
    index=int(a[1]);
    label[index]=int(a[0]);
    n+=1;
    l=f.readline();
    
#Use mutual information to do feature selection

mi=[0]*m;
for j in range(0,m):
    fy=[0]*2;
    fx=[0]*3;
    fyx=[];
    fyx.append([0]*3);
    fyx.append([0]*3);
    
    for i in range(0,nd):
        y=label[i];
        if(y==-1):
            continue;
        x=data[i][j];
        fx[x]+=1;
        fy[y]+=1;
        fyx[y][x]+=1;
    for y in range(0,2):
        for x in range(0,3):
            if(fyx[y][x]>0):
                t=fyx[y][x]*n/(fx[x]*fy[y]);
                if(t<=0):
                    continue;
                mi[j]+=fyx[y][x]/n*math.log2(t);
    print(j," ",mi[j]);



### Prediction
f1=open("mutual_information", "w+");
for j in range(0,m):
    f1.write(str(mi[j])+'\n');
f1.close();
