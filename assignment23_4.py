import pandas as pd
import numpy as np

data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [85, 90, 78],
            'science' : [92, 88, 80],
            'english' : [75, 85, 82]}

df = pd.DataFrame(data)

print("students who score who score more that 85 in science :")

print(df[df['science'] > 85])