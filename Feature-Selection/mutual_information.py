import sys
import math

### read data
f=open(sys.argv[1]);
boundry=100;

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
n=len(data);
m=len(data[0]);

### read train labels
f=open(sys.argv[2]);
label=[-1]*n;
l=f.readline();
while(l!=''):
    a=l.split();
    index=int(a[1]);
    label[index]=int(a[0]);
    l=f.readline();
    
#Use mutual information to do feature selection

mi=[0]*m;
for j in range(0,m):
    py=[0]*2;
    px=[0]*3;
    pyx=[];
    pyx.append([0]*3);
    pyx.append([0]*3);
    
    for i in range(0,n):
        y=label[i];
        x=data[i][j];
        px[x]+=1/n;
        py[y]+=1/n;
        pyx[y][x]+=1/n;
    for y in range(0,2):
        for x in range(0,3):
            if(pyx[y][x]>0):
                t=pyx[y][x]/(px[x]*py[y]);
                if(t<=0):
                    continue;
                mi[j]+=pyx[y][x]*math.log2(t);
    print(j," ",mi[j]);



### Prediction
f1=open("mutual_infomation", "w+");
for j in range(0,m):
    f1.write(str(mi[j])+'\n');
f1.close();
