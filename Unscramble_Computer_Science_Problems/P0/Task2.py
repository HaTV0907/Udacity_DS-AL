"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
nums = []
for num in calls:
    nums.append(num[0])
    nums.append(num[1])
# create a set of number
unique_nums = set(nums)
# dict contain number and call duration
callDuration = dict()
for unique_num in unique_nums:
    for num in calls:
        if unique_num == num[0] or unique_num == num[1]:
            if callDuration.get(unique_num) == None:
                callDuration[unique_num] = int(num[3])
            else:
                callDuration[unique_num] += int(num[3])

# Convert the dictionary into a list of tuples
call_list = list(callDuration.items())

# Sort the list based on the values (second element of each tuple)
sorted_list = sorted(call_list, key=lambda x: x[1], reverse=True)

print(sorted_list[0][0] + " spent the longest time, " + str(sorted_list[0][1]) + " seconds, " +\
       "on the phone during September 2016.")

