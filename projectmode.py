import csv
from collections import Counter

with open('data!!.csv',newline='') as f :
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    n_number=filedata[i][1]
    newdata.append(float(n_number))

data=Counter(newdata)

mode_data_for_range={
    "60-90":0,
    "90-100":0,
      
}
for height,occurrence in data.items():
    if 50<float(height)<60:
        mode_data_for_range["60-90"]+= occurrence
    elif 60<float(height)<70:
        mode_data_for_range["90-100"]+= occurrence    
     

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
