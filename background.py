import numpy as np
import pandas as pd

import plotly
import plotly.graph_objs as go
from plotly.offline import *

df = pd.read_csv('processed.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(253,224,221)'], [0.1, 'rgb(250,159,181)'],
       [1.0, 'rgb(197,27,138)']]

df['text'] = df['state'] + '<br>' +\
    'Number of Firearm Background Checks per 100,000 people: '+df['background_rate']

data = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=df['code'],
    z=df['background_rate'].astype(float),
    locationmode='USA-states',
    text=df['text'],
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )),
    colorbar=dict(
        title="Background Check Rate per 100,000")
)]

layout = dict(
    title='Number of Background Checks per 100,000 people',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='background_map')
