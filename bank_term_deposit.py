import pandas as pd

test_data = pd.read_csv("data/test.csv")
train_data = pd.read_csv("data/train.csv")

# print test data
print(f'\nTest Data:\n\n\n{test_data}\n\n\n\n')
#print train data
print(f'Train Data:\n\n\n{train_data}')