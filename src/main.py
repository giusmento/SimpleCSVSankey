import pandas
import plotly
import plotly.graph_objects as go
from sankey import genSankey 

df = pandas.read_csv("./data/data.csv")
fig = genSankey(df, cat_cols=['Question1','Question2','Question3','Question4'], title='Sankey Diagram')
plotly.offline.plot(fig, validate=False)