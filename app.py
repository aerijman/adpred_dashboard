#!/usr/bin/env python

import dash
import dash_html_components as html
import dash_core_components as dcc
import pickle
import numpy as np
from dash.dependencies import Input, Output


# 'sequence', 'prediction', 'ss', 'heatmaps']


# load data
#with open('data/Kenneth.pkl', 'rb') as f:
with open('data/proteins.pkl', 'rb') as f:
    proteins = pickle.load(f)

# Initialize app with pre-defined style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# define the layout          
app.layout = html.Div(
                children = [
                    # title
                    html.H3(children="Adpred results", style={'textAlign': 'center'}),

                    html.Div([
                        html.Label('Choose a TF'),
                        dcc.Dropdown(
                            id='select TF',
                            options=[{'label':k, 'value':k} for k in proteins.keys()],
                            value=list(proteins.keys())[0]),
                        html.Label('Choose start position'),
                        dcc.Dropdown(id='heatmap items'),
                    ], style={'width': '15%', 'padding': '0px 0px -40px 0px', 'margin':'100px 0px 0px 0px'}),
                
                    html.Div([
                        html.Div([  dcc.Graph(id='profile'), ], style={'width':'100%', 'margin': '0px 0px -40px 0px','padding': '0px 0px 0px 0px'}), 
                        html.Div([  dcc.Graph(id='heatmap')], style={'width':'50%',  'padding': '0px 40px -30px 0px'}),
                        ], style={'width': '75%', 'align': 'right', 'padding': '10px 0px 0px 50px', 'margin': '-230px 0px 0px 250px'})
                    ])



@app.callback(
    Output('profile', 'figure'),
    [Input('select TF', 'value')])   
def update_profile(TF):
    return  {
            'data': [{
                'x': np.arange(len(proteins[TF]['predictions'])),
                'y': np.convolve(proteins[TF]['predictions'], np.ones(15)/15, 'same'), 
                'mode':'lines+markers',
                'opacity':0.7,
                'marker':{
                'size': 5,
                'line': {'width': 0.5, 'color': 'white'}},
                'text': list(proteins[TF]['sequence']),
                'hovertemplate': "Id: %{text}<br>position: %{x}<br>adpred-score: %{y}", 
                'name':'test'}],
            "layout": {"height":500, 
                       'xaxis':{'title': '..                           position'},
                       'yaxis':{'title': 'adpred score'}
                        }, 
                       #'margin':{'t': -800, 'b': -900}}
            }


@app.callback(
    [Output('heatmap items', 'options'),
     Output('heatmap items', 'value')],
    [Input('select TF','value')])
def update_heatmap_slider(TF):  #'SREBF1'
    marks = [k for k,v in proteins[TF]['heatmaps'].items() if v!=[]]    
    # if there are no 30mers with satu mut analysis
    if marks == []: 
        return [{'label':'None', 'value':0}],1
    options=[{'label':i, 'value':i} for i in marks]    
    value=marks[0]
    return options, value 
    

@app.callback(
    Output('heatmap','figure'),
    [Input('select TF','value'),
     Input('heatmap items','value')])
def update_heatmap(TF, start_pos):
    aa = ['R','H','K','D','E','S','T','N','Q','A','V','L','I','M','F' ,'Y', 'W', 'C','G','P']
    return { 
        'data': [{
            'z': proteins[TF]['heatmaps'][start_pos],
            'type': 'heatmap',}],
        'layout': {
            'xaxis':{
                'tickvals': np.arange(30),
                'ticktext': list(proteins[TF]['sequence'][start_pos:start_pos+30])},
            'yaxis':{
                'tickvals': np.arange(20),
                'ticktext': aa[::-1]},
            'title':'saturated mutagenesis'}
    }
    

if __name__ == "__main__":
    app.run_server(debug=True)
