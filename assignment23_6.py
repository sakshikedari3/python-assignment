import pandas as pd
import numpy as np

data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [85, 90, 78],
            'science' : [92, 88, 80],
            'english' : [75, 85, 82]}

df = pd.DataFrame(data)

df['total'] = df['math'] + df['science'] + df['english']

print(df)

df.sort_values(by='total', ascending=False, inplace=True)

print("updated df :")
print(df)
