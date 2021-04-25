import csv

with open('data!!.csv',newline='') as f :
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    n_number=filedata[i][1]
    newdata.append(float(n_number))
#from line 12 we are calculating mean value !
n=len(newdata)
total=0
for x in newdata:
    total += x
  
 nm  print(total)   
#mean=total/n
#print(mean)          







