# INTRODUCTION
This project contain execution python file and all the necessary input data files, which have names such as class1.txt, class2.txt,... These files contain the data of students with their ids and their answers for the exam. However, some of the lines in the data are not well-formed. 

The purpose of this project is to filter out the fault data and give us some insight into the exam results of each class.

---
# HOW TO USE
## STEP 1: Download the project:
`git clone https://github.com/ductran17/Funix_assignment2.git`

## STEP 2: Run the project:
1. **Move to the project directory**
2. **Start:**

    `python3 lastname_firstname_grade_the_exams.py`

3. **Input the class name you want to execute with the project (for e.g: class1)**

    A file which contains the exam result of each student will be generate in the same directory of the project. You should also see the output of the project on the command line which includes: 
    - Overall analysis result
    - Invalid line of data 
    - Total student of high scores
    - Mean (average) score
    - Highest score
    - Lowest score
    - Range of scores
    - Median score
    - Question that most people skip
    - Question that most people answer incorrectly


    **Example of terminal output (class1):**

        Enter the class name to open (i.e. class for class1.txt) class1

        Successfully opened class file with name: class1

        **** ANALYZING ****

        No errors found!

        **** REPORT ****

        Total valid lines of data: 20

        Total invalid lines of data: 0

        Total student of high scores:  6

        Mean (average) score:  75.6

        Highest score:  91

        Lowest score:  59

        Range of scores:  32

        Median score:  73.0

        Question that most people skip: 3-4-0.2 , 5-4-0.2 , 23-4-0.2

        Question that most people answer incorrectly: 22-4-0.2 , 19-4-0.2 , 16-4-0.2 , 14-4-0.2 , 10-4-0.2

    **Example of result output file (class1):**

        N00000001,59

        N00000002,70

        N00000003,84

        N00000004,73

        N00000005,83

        N00000006,66

        N00000007,88

        N00000008,67

        N00000009,86

        N00000010,73

        N00000011,86

        N00000012,73

        N00000013,73

        N00000014,78

        N00000015,72

        N00000016,91

        N00000017,66

        N00000018,78

        N00000019,78

        N00000020,68


