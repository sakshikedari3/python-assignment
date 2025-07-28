import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [85, 90, 78],
            'science' : [92, 88, 80],
            'english' : [75, 85, 82]}

df = pd.DataFrame(data)

marks = df[df['name'] == 'amit'][['math','science','english']].values.flatten()#convert 2d into 1d

subjects = ['math','science','english']

plt.plot(subjects, marks, marker = "o")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("amit report")
plt.grid(True)
plt.show()