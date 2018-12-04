import csv

csv_file = csv.reader(open('/Users/macbook/Desktop/map_addresses-1_500000.csv', 'rt'), delimiter=',')
for row in csv_file:
    print(row)
