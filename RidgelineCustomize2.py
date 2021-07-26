# !pip install joypy

import pandas as pd
from joypy import joyplot
import matplotlib.pyplot as plt
from matplotlib import cm

df = pd.read_csv("Admission_Predict.csv")


df['University Rating'] = df['University Rating'].astype(str)

joyplot(df, by = 'University Rating', column = 'CGPA', colormap = cm.autumn, fade = True, range_style='own', figsize = (10,6), 
        title = 'Distribution of Student CGPA based on University Rating')
plt.xlabel("CGPA")


plt.show()
