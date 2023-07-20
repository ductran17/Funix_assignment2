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
id_answers = []
faults = []
for line in lines:
    match = re.match(regex, line)
    if match:
        id_answers.append(line)
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
answers_key = np.array(answers_key)
# Using pandas to turn all the answers into dataframes
num_of_col = 25
df = pd.DataFrame({f'question_{i+1}': []
                   for i in range(num_of_col)})
for e in id_answers:
    e = re.split(',', e)
    id = e[0]
    answer = e[1:]
    answer = np.array(answer)
    point = (answer == answers_key)*4 + \
        ((answer != '') & (answer != answers_key))*(-1)
    df.loc[id] = point
df['total_point'] = [df.loc[index].sum()
                     for index in list(df.index)]
print(df)
print("Total student of high scores: ", len(df[df["total_point"] > 80]))
print("Mean (average) score: ", df['total_point'].mean().round(3))
print("Highest score: ", df["total_point"].max())
print("Lowest score: ", df["total_point"].min())
print("Range of scores: ", df['total_point'].max()-df['total_point'].min())
print("Median score: ", df["total_point"].median())
# TASK 3.7+3.8
# create a series of all questions along with the number of students who dont know the answer for each question
skip_ans = pd.Series()
false_ans = pd.Series()
for q in list(df.columns)[:-1]:
    ques_stat = df[q].value_counts()
    # if a question is skipped, it means the poin for it is 0
    if 0 in list(ques_stat.index):
        skip_ans[q] = ques_stat[0]
    else:
        skip_ans[q] = 0
    # if a question is skipped, it means the poin for it is -1
    if -1 in list(ques_stat.index):
        false_ans[q] = ques_stat[-1]
    else:
        false_ans[q] = 0

# print the most skipped questions
skip_ans = skip_ans.sort_values(ascending=False)
max_skip = skip_ans[skip_ans == skip_ans.max()]
print("Question that most people skip: ", end="")
for i in list(max_skip.index):
    if i != list(max_skip.index)[0]:
        print(' , ', end="")
    print("{}-{}-{}".format(i[9:], max_skip[i],
          round(max_skip[i]/len(df), 3)), end="")
print("\n")
# print the questions that are most wrongly answered
false_ans = false_ans.sort_values(ascending=False)
max_fault = false_ans[false_ans == false_ans.max()]
print("Question that most people answer incorrectly: ", end="")
for i in list(max_fault.index):
    if i != list(max_fault.index)[0]:
        print(' , ', end="")
    print("{}-{}-{}".format(i[9:], max_fault[i],
          round(max_fault[i]/len(df), 3)), end="")
