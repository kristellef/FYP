import numpy as np
import csv

mapping_csv = csv.reader(open('/Users/macbook/Desktop/mapping-darknet.csv', 'rt'), delimiter=',')
writer = csv.writer(open('/Users/macbook/Desktop/mapping-darknet copy.csv', 'wt'))
npyarray=[]
count=0
data = []
data = np.load('/Users/macbook/Desktop/minimise_user-1_500000.npy')

for row in mapping_csv:
    index = int(row[2])
    npyarray.append(data[index])
    count += 1
    if count % 1000 == 0:
        print(count, '/1.817.311')

np.save('/Users/macbook/Desktop/output.npy', npyarray)

print('done')

