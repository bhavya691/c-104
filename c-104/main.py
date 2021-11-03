import csv
from collections import Counter
# with open('height-weight.csv', newline = '') as f:
#     reader = csv.reader(f)
#     file_data = list(reader)
#     print(file_data)

x = 'Bhavya Raj Deora'
data = Counter(x)
y = data.items()
print(data)
print(y)