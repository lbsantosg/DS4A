import dash
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import dash_trich_components as dtc



register_page(__name__, path="/cuestionario")

slider = html.Div(
    [
        dbc.Label("Slider", html_for="slider"),
        dcc.Slider(id="slider", min=0, max=10, step=0.5, value=3),
    ],
    className="mb-3",
)

form_p= html.Div([
                dbc.Label("Email", html_for="example-email"),
                dbc.Input(type="email", id="example-email", placeholder="Enter email"),
                dbc.FormText(
                    "Are you on email? You simply have to be these days",
                    color="secondary"
                )                
            ])

carousel = dtc.Carousel([
            html.Div([
                dbc.Label("Email", html_for="example-email"),
                dbc.Input(type="email", id="example-email", placeholder="Enter email"),
                dbc.FormText("Are you on email? You simply have to be these days", color="secondary"),
                dbc.Label("Slider", html_for="slider"),
                dcc.Slider(id="slider", min=0, max=10, step=1, value=3),
            ],
            className="card"),
            
            form_p,
            slider
          ],

            
        arrows= True,    
        infinite=False,
        slides_to_show=1,
        slides_to_scroll=1,
        swipe_to_slide=False     
		)

layout= dbc.Container(
    [
        carousel
    ],
    className="dbc content",
    fluid=True,
)