
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

css_url = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
app.css.append_css({'external_url': css_url})

df = pd.read_excel('H:\\My Documents\\webprojects\\dash_apps\\boards\\f1racing\\data\\final_results2005_2017.xlsx', encoding='latin-1')

headtop = 50
mleft = 30
mtop = 20



race_list = df['race'].unique()
year_list = df['year'].unique()

app.layout = html.Div([

    html.Div([
        html.Div([
            html.H1('Formula 1 Racing Results', className = 'col-md-12')
        ], className = 'display-3'),
    ], className = 'row', style = {'margin-top': headtop, 'margin-left': mleft}),

          #####################  controls   ##################################    

    html.Div([    
        
        html.Div([
            
            dcc.Dropdown(
            id = 'years_cntrl',
            options = [{'label': i, 'value': i} for i in year_list],
            value = '2005')   
        ], className = 'col-md-2'),

        html.Div([
            dcc.Dropdown(
                id = 'race_names_cntrl',
                options = [{'label': i, 'value': i} for i in race_list],
                value = 'Australian Grand Prix')
        ], className = 'col-md-2')


    ], className = 'row', style = {'margin-top': mtop, 'margin-left': mleft}),


           #################  graphs section  #############################
    html.Div([

        html.Div([
            dcc.Graph(id='driver_results', config = {'displayModeBar': False})
        ], className = 'col-md-6'),

        html.Div([
            dcc.Graph(id='driver_pts', config = {'displayModeBar': False})
        ], className = 'col-md-6'),

    ], className = 'row', style = {'margin-top': mtop, 'margin-left': mleft}),

    html.Div([
    
        html.Div([
            dcc.Graph(id='const_pts', config = {'displayModeBar': False})
        ], className = 'col-md-6')

        #html.Div([
           # html.H1('some text')


        #], className = 'col-md-6')

    ], className = 'row', style = {'margin-top': mtop, 'margin-left': mleft})


])




############## callback driver results graph  ################################

@app.callback(
    dash.dependencies.Output('driver_results', 'figure'),
    [dash.dependencies.Input('race_names_cntrl', 'value'),
    dash.dependencies.Input('years_cntrl', 'value')]



)

##################### driver results graph code  #################################

def drawDriverResults(race_names_cntrl, years_cntrl):
    
    dff = df[(df.race == race_names_cntrl) & (df.year == years_cntrl)]
    

    return {
    'data': [
        {
        'type': 'scatter',
        'x': dff['driver'],
        'y': dff['grid'],
        'name': 'Grid Position',
        'mode': 'markers',
        'opacity': 0.4,
        'marker': {'size': 15, 'color': 'rgb(155, 165, 195)'}
        },
        
        {
        'type': 'scatter',
        'x': dff['driver'],
        'y': dff['driver_finish'],
        'name': 'Finish Position',
        'mode': 'markers',
        'opacity': 0.7,
        'marker': {'size': 15, 'color': 'rgb(185, 45, 0)'}
        }
    
    ],
    
    'layout': {'title': 'Grid & Finish Positions',
              #'margin': {'l': 175, 'r': 75, 'b': '125'},
              #'width': 900,
              #'height': 500,
              'yaxis': {'title': 'Positions'},
              'xaxis': {'title': 'Driver'}
              }  


    }

############## callback driver points  ################################

@app.callback(
    dash.dependencies.Output('driver_pts', 'figure'),
    [dash.dependencies.Input('race_names_cntrl', 'value'),
    dash.dependencies.Input('years_cntrl', 'value')]


)


##################### driver points graph code  #################################

def drawDriverPts(race_names_cntrl, years_cntrl):
    
    dff = df[(df.race == race_names_cntrl) & (df.year == years_cntrl)]
    
    

    return {

    'data': [
        {
        'type': 'scatter',
        'x': dff['driver_pts'],
        'y': dff['driver'],
        'mode': 'markers',
        'opacity': 1.0,
        'marker': {'size': 15,'color': 'rgb(180, 210, 190)'}
        }
    ],
    
    'layout': {'title': 'Driver Points by Race',
              'xaxis': {'title': 'Points'},
              'yaxis': {'title': 'Driver'},
              'showlegend': False,
              #'margin': {'l': 150, 'r': 75, 'b': 150},
              #'width': 900,
              #'height': 500
              }  

    }



############## callback constructor points  ################################

@app.callback(
    dash.dependencies.Output('const_pts', 'figure'),
    [dash.dependencies.Input('race_names_cntrl', 'value'),
    dash.dependencies.Input('years_cntrl', 'value')]


)


##################### constructor points graph code  #################################

def drawConstPts(race_names_cntrl, years_cntrl):
    
    dff = df[(df.race == race_names_cntrl) & (df.year == years_cntrl)]
    
    

    return {

    'data': [
        {
        'type': 'bar',
        'x': dff['constructor'],
        'y': dff['constructor_pts'],
        'text': dff['constructor_pts'],
        'textposition': 'auto',
        'textfont': {'family': 'Arial', 'size': 14, 'color': 'rgb(0, 0, 0)'},
        'opacity': 0.7,
        'hoverinfo': 'none',
        'marker': {'color': 'rgb(80, 140, 240)'}
        }
    ],
    
    'layout': {'title': 'Constructor Points',
               'yaxis': {'showline': False, 'showticklabels': False, 'showgrid': False},
              'showlegend': False,
              #'margin': {'l': 150, 'r': 75, 'b': 150},
              #'width': 900,
              'height': 275
              }  

    }








if __name__ == '__main__':
    app.run_server(
        host = '127.0.0.1',
        port = 8050,
        debug=True
    )

