import regex as re
import numpy as np
import pandas as pd

# Task 1
while True:
    filename = input(
        "Enter the class name to open (i.e. class for class1.txt) \n")
    try:
        f = open(filename+".txt")
        print("Successfully opened class file with name:", filename)
        break
    except:
        print("Cannot find file with name:", filename)

# Task 2
print("**** ANALYZING ****")
content = f.read()
lines = re.split('\n', content)
regex = 'N[0-9]{8}(?:,[A-D]?){25}$'
answers = []
faults = []
for line in lines:
    match = re.match(regex, line)
    if match:
        answers.append(line[10:])
    else:
        faults.append(line)
if (len(faults) == 0):
    print("No errors found!")
else:
    for fault in faults:
        faultElements = re.split(',', fault)
        if len(faultElements) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(fault)
        elif not re.match('N[0-9]{8}', faultElements[0]):
            print("Invalid line of data: N# is invalid")
            print(fault)
        else:
            print("Invalid line of data: Unknown reason")

print("**** REPORT ****")
print("Total valid lines of data:", len(lines)-len(faults))
print("Total invalid lines of data:", len(faults))

# Task 3

answers_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answers_key = re.split(',', answers_key)
marks = []
for answer in answers:
    i = 0
    mark = 0
    answer = re.split(',', answer)
    while i < 25:
        if answer[i] != '':
            if answer[i] == answers_key[i]:
                mark += 4
            else:
                mark -= 1
        i += 1
    marks.append(mark)
marks = np.array(marks)
print("Total student of high scores: ", round(marks[marks > 80], 3))
print("Mean (average) score: ", round(marks.mean(), 3))
print("Highest score: ", round(marks.max(), 3))
print("Lowest score: ", round(marks.low(), 3))
print("Range of scores: ", round(marks.max()-marks.min(), 3))
print("Median score: ", round(marks.median(), 3))


print(marks.mean())
