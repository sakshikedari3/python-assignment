import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [np.nan, 90, 78],
            'science' : [92, 88, np.nan]}

df = pd.DataFrame(data)

print(df)

df.fillna(df.mean(numeric_only=True), inplace = True)

print(df)