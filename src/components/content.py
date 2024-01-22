# import dash_core_components as dcc
from dash import dcc, html
import glob
import os
import plotly.graph_objs as go
import plotly.express as px
import pyvista as pv


def load_vtk_data(vtk_files):
    traces = []
    colors = px.colors.qualitative.Plotly  # A list of colors for plots

    for i, file in enumerate(vtk_files):
        mesh = pv.read(file)

        x, y, z = mesh.points.T
        faces = mesh.faces.reshape((-1, 4))[:, 1:4].flatten()

        color = colors[i % len(colors)]  # Cycle through colors

        trace = go.Mesh3d(
            x=x, y=y, z=z, 
            i=faces[::3], j=faces[1::3], k=faces[2::3],
            color=color,
            name=os.path.basename(file).split('_')[-1]  # Use file name as trace name
        )
        traces.append(trace)

    return traces


def create_plotly_figure(traces):
    fig = go.Figure(data=traces)
    fig.update_layout(
        scene=dict(aspectmode='data'),
        # legend=dict(title='VTK Files', itemsizing='constant'),
        showlegend=True,
        legend=dict(
            title='VTK Files',
            x=1,
            y=0,
            xanchor='right',
            yanchor='bottom',
            bgcolor='rgba(255, 255, 255, 0.5)',  # Optional: semi-transparent white background
            bordercolor='Black',
            borderwidth=1
        ),
        margin=dict(r=500)
    )
    return fig



def Content():
    #vtk_files = glob.glob('src/data/*.vtp')  # List of VTK files
    data_dir = os.path.join(os.path.dirname(__file__), '../data/')
    vtk_files = glob.glob(os.path.join(data_dir, '*.vtp'))
    traces = load_vtk_data(vtk_files)

    plotly_figure = create_plotly_figure(traces)

    content = dcc.Graph(
                id='3d-plot',
                figure=plotly_figure,
                style={'height': '800px'},
                )
        

    return content
