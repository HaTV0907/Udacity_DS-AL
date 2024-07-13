"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
nums = []
for num in texts:
    nums.append(num[0])
    nums.append(num[1])
for num in calls:
    nums.append(num[0])
    nums.append(num[1])

unique_nums = set(nums)
# print(texts)
print("There are " + str(len(unique_nums)) + " different telephone numbers in the records.")