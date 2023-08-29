import pandas as pd
from itertools import combinations


def isPotentialKey(columns):
    subset = data[list(columns)]
    if len(subset) == len(subset.drop_duplicates()):
        for key in candidate_keys:
            if set(columns).issuperset(set(key)):
                return False
        return True
    return False


data = pd.read_excel('Table.xlsb', header=None, skiprows=1)
data = data.drop(data.columns[0], axis=1)
correct_column_names = data.iloc[0]
data = data.iloc[1:]
data.columns = correct_column_names

candidate_keys = []

for num_columns in range(1, len(data.columns) + 1):
    column_combinations = combinations(data.columns, num_columns)
    for columns in column_combinations:
        if isPotentialKey(columns):
            candidate_keys.append(columns)
            print(columns)

for key in candidate_keys:
    print("Candidate key:", key)

print("Общее число candidate keys:", len(candidate_keys))
