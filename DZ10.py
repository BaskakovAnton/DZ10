import random
import pandas as pd

random.seed(42)  # for reproducibility
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Create one-hot encoded columns manually
one_hot_data = pd.DataFrame({'whoAmI_robot': [1 if value == 'robot' else 0 for value in data['whoAmI']],
                             'whoAmI_human': [1 if value == 'human' else 0 for value in data['whoAmI']]})

# Concatenate the original DataFrame with the one-hot DataFrame
data = pd.concat([data, one_hot_data], axis=1)

# Drop the original 'whoAmI' column
data = data.drop('whoAmI', axis=1)

data.head()
