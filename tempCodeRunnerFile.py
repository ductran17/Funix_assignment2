import pandas as pd
# print("Mean (average) score: ", round(marks.mean(), 3))
# print("Highest score: ", round(marks.max(), 3))
# print("Lowest score: ", round(marks.low(), 3))
# print("Range of scores: ", round(marks.max()-marks.min(), 3))
# print("Median score: ", round(marks.median(), 3))
idx = pd.Index(['Harry', 'Mike', 'Arther', 'Nick',
                'Harry', 'Arther'], name='Student')
ic = idx.value_counts()
print(ic['a'])
