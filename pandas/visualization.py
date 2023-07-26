import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Visualization in Pandas

# Creating a Series to work with
ts = pd.Series(np.random.randn(50), index=pd.date_range('today', periods=50))
print(ts)

# Plotting the cumulative sum of all the values
ts = ts.cumsum()
ts.plot()

# Creating a DataFrame to work with
df = pd.DataFrame(np.random.randn(50, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()

# figure out how work this in pycharm

#Removing Repeated Data
df2 = pd.DataFrame({'A': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8]})
print(df2)
print(df2.loc[df2['A'].shift() != df2['A']])



