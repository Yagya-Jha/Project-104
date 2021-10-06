print("Weight of an 18 year old person (Pounds)", '\n')


import csv
with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
new_data = []
for i in range(len(filedata)):
    n_num = filedata[i][2]
    new_data.append(float(n_num))

n = len(new_data)
total = 0

for j in new_data:
    total+=j

mean = total/n

# Print Mean
print("Mean is -> ", mean)

n = len(new_data)
new_data.sort()
if n%2==0:
    m1 = float(new_data[n//2])
    m2 = float(new_data[n//2-1])
    median = (m1+m2)//2
else:
    median = new_data[n//2]

# Print Median
print("The Median is -> ", median)

from collections import Counter

data = Counter(new_data)
mode_data_range = {
    "50 - 60": 0,
    "60 - 70": 0,
    "70 - 80": 0
}

for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_range["50 - 60"]+= occurence
    elif 60 < float(height) <70:
        mode_data_range["60 - 70"]+=occurence
    elif 70 < float(height) < 80:
        mode_data_range["70 - 80"]+=occurence

mode_range = 0
mode_occurence = 0

for range, occurence in mode_data_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        mode = float((mode_range[0]+mode_range[1]) / 2)

        print('Mode is -> ', mode)

quit = input("You Can Quit Now")