import csv
import plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot
# init_notebook_mode(connected=True)

plotly.tools.set_credentials_file(username='RuizhiYang', api_key='Sl4pN9nzBpUi2KBVuaF7')

print('1. start to parse data.')
with open('testdata.csv', 'r', encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file)
    old_rows = [row for row in reader]

'''
shot_trace = go.Scatter(
    x=[row[2] for row in old_rows],
    y=[row[3] for row in old_rows],
    mode='markers'
)

'''

x = []
y = []
for row in old_rows:
    if row[1] == '0':
        x.append(row[2])
        y.append(row[3])

missed_shot_trace = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Missed Shot',
    marker=dict(
        symbol='x',
        size=8,
        color='rgba(255, 0, 0, .8)',
        line=dict(
            width=1,
            color='rgb(0, 0, 0, 1)'
        )
    )
)

x = []
y = []
for row in old_rows:
    if row[1] == '1':
        x.append(row[2])
        y.append(row[3])


made_shot_trace = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Made Shot',
    marker=dict(
        size=8,
        color='rgba(0, 200, 100, .8)',
        line=dict(
            width=1,
            color='rgb(0, 0, 0, 1)'
        )
    )
)

data = [missed_shot_trace, made_shot_trace]
layout = go.Layout(
    title='Shots by Micheal Jordan in NBA2K11 shootout session',
    showlegend=True,
    height=800,
    width=1000,
    scene=dict(aspectmode="data")
)

fig = go.Figure(data=data, layout=layout)
plot(fig)