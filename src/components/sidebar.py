from dash import dcc
from dash import html

def Sidebar():
    sidebar = html.Div([
        html.H2('Controls', style={'text-align': 'center'}),
        html.Div([
            html.Label('Orientation'),
            dcc.Slider(
                id='orientation-slider',
                min=0,
                max=360,
                step=1,
                value=180,
                marks={i: str(i) for i in range(0, 361, 45)}
            ),
            html.Label('Distance'),
            dcc.Slider(
                id='distance-slider',
                min=0,
                max=100,
                step=1,
                value=50,
                marks={i: str(i) for i in range(0, 101, 10)}
            ),
            # Add more controls here as needed
        ], style={'padding': '20px'})
    ], style={
        'border': 'thin lightgrey solid',
        'padding': '10px',
        'margin': '10px'
    })

    return sidebar
