import pandas as pd
from itertools import combinations

data = pd.read_excel('Table.xlsb', header=None, skiprows=1)
data = data.drop(data.columns[0], axis=1)
correct_column_names = data.iloc[0]
data = data.iloc[1:]
data.columns = correct_column_names

candidate_keys = []

for num_columns in range(1, len(data.columns) + 1):
    column_combinations = combinations(data.columns, num_columns)
    for columns in column_combinations:
        subset = data[list(columns)]

        if len(subset) == len(subset.drop_duplicates()):
            candidate_keys.append(columns)

for key in candidate_keys:
    print("Candidate key:", key)
print("Общее число candidate keys:", len(candidate_keys))
