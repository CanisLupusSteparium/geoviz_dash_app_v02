from dash import html

def Navbar():
    navbar = html.Div([
        html.Div([
            html.H2('EAS 233 : Model Visualization', style={'margin-left': '20px'}),
            # You can add more navbar items here
        ], className="row")
    ], className="navbar")

    return navbar
