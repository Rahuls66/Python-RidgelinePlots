# !pip install joypy

import pandas as pd
from joypy import joyplot
import matplotlib.pyplot as plt

df = pd.read_csv("Admission_Predict.csv")
# print(df.info())

df['University Rating'] = df['University Rating'].astype(str)

joyplot(df, by = 'University Rating', column = 'CGPA')
plt.xlabel("CGPA")

plt.show()
