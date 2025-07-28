import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [85, 90, 78],
            'science' : [92, 88, 80],
            'english' : [75, 85, 82]}

df = pd.DataFrame(data)

df['total'] = df['math'] + df['science'] + df['english']

plt.bar(df['name'], df['total'])
plt.xlabel("students marks")
plt.ylabel("total marks")
plt.title("marks")
plt.show()