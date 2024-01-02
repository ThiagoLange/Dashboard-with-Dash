from dash import Dash,dcc, html
import pandas as pd
import dash_bootstrap_components as dbc

# Initialize the Dash app and import the Bootstrap theme to style the dashboard
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dcc.Store(id='store'),
        html.H1('Netflix Movies and TV Shows Dashboard'),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label='Geographical content distribution', tab_id='tab1'),
                dbc.Tab(label='Content classification', tab_id='tab2'),
            ],
            id='tabs',
            active_tab='tab1',
        ),
        html.Div(id='tab-content', className='p-4'),
    ]
)

if __name__ == '__main__':
    app.run(debug=True)