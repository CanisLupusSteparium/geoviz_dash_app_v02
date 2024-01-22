import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import glob
from components.navbar import Navbar
from components.sidebar import Sidebar
from components.content import Content, load_vtk_data, create_plotly_figure
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Expose the server for deployment
server = app.server

# Define the app layout
app.layout = html.Div([
    Navbar(),
    Content(),
])

# Define callback for updating plots (placeholders for now)
@app.callback(
    Output('3d-plot', 'figure'),
)
def update_plots():
    vtk_files = glob.glob('data/*.vtp')  # List of VTK files
    traces = load_vtk_data(vtk_files)

    plotly_figure = create_plotly_figure(traces)

    return plotly_figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
