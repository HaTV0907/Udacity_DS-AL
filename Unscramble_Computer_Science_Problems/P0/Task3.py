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

areaCodes = []
for call in calls:
    areaCode = None
    # check whether caller is having Bangalore fixed line no. or not.
    if call[0].startswith("(080)"):
        # if call[1] is fixed line no, fetch area code else
        if call[1].startswith("(0"): # check "(0" instead of "(0)" - func areaCode()
            areaCode = call[1][0:call[1].find(')')+1]
        # if call[1] is mobile number, fetch area code else
        if call[1].startswith(('7', '8', '9')):
            areaCode = call[1][0:4]
        # if call[1] is telemarketer number, fetch the area code
        if call[1].startswith("140"):
            areaCode = "140"
    if None != areaCode:
        areaCodes.append(areaCode)
#sort the resultant list/set and display.
areaCodes = list(set(areaCodes))
print("The numbers called by people in Bangalore have codes:")
for code in sorted(areaCodes):
    print(code)

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