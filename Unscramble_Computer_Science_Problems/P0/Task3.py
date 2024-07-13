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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def char_in_str(text: str, char: str) -> bool:
    if char in text:
        return True

def telemarketers(num:str) -> bool:
    return num.startswith("140") and not char_in_str(num, " ") \
           and not char_in_str(num, "(") and not char_in_str(num, ")")

def mobile(num:str) -> bool:
    if num.startswith("7") or num.startswith("8") or num.startswith("9") \
        and not char_in_str(num, "(") and not char_in_str(num, ")") \
        and not char_in_str(num, ' '):
          return True

def areaCode(num:str) -> bool:
    if num.startswith("(0)"):
        return True
recivers = []
# create a list of received of numbers called from people in Bangalore
for num in calls:
    if num[0].startswith("(080)"):
        recivers.append(num[1])

# make received list unique
uniqueReceivers = set(recivers)
numList = list(uniqueReceivers)
results = []
for num in numList:
    if telemarketers(num) or mobile(num) or areaCode(num):
        results.append(num)

print("The numbers called by people in Bangalore have codes:")
for num in results:
    print(num)

# Task B
fromBangalore = []
toBangalore = []
for num in calls:
    if num[0].startswith("(080)"):
        fromBangalore.append(num)
        if num[1].startswith("(080)"):
            toBangalore.append(num)

percent = round(len(toBangalore)/len(fromBangalore) * 100, 2)
print( str(percent) + " percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.")