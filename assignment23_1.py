import pandas as pd
import numpy as np

data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [85, 90, 78],
            'science' : [92, 88, 80],
            'english' : [75, 85, 82]}

df = pd.DataFrame(data)

print("shape :",df.shape)
print("columns :",df.columns)
print("datatype :",df.dtypes)

