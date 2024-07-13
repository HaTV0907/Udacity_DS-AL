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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
callNums = []
receiveNums = []
textNums = []
for num in texts:
    textNums.append(num[0])
    textNums.append(num[1])

for num in calls:
    callNums.append(num[0])
    receiveNums.append(num[1])

def telemaketers(num: str) -> bool:
    if num not in textNums \
       and num not in receiveNums:
        return True
# make call list contains unique number
callNums = list(set(callNums))

teleNums = []
for num in callNums:
    if telemaketers(num):
        teleNums.append(num)

print("These numbers could be telemarketers: ")
for num in teleNums:
    print(num)