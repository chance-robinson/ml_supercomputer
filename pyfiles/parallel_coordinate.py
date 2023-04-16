import pandas as pd
import plotly.express as px
import os

os.chdir('..')
cwd = os.getcwd()

df = pd.read_csv('{cwd}/content/parameter_sweep.csv')

fig = px.parallel_coordinates(df, color='VAL_ACCURACY', color_continuous_scale=px.colors.sequential.Viridis[::-1])

fig.show()
