#libraries
from pydoc import classname
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
from dash import Input, Output, dcc, html
import dash_trich_components as dtc



# Dash instance declaration , using icons from font awesome
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.icons.BOOTSTRAP])

#Top navbar
navbar = dbc.NavbarSimple(
    [
        html.A([ html.Img(src="./assets/images/logo.png", height="52px") ],  href="/"     
    )],
    dark=True,
    class_name="",
    sticky="top",
)

#Creating sidebar, to insert content on page use className : content
sidebar = html.Div(
    [        
        dbc.Nav(
            [
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.NavLink([html.I(className="bi bi-house-fill ic"),"Realizar Test"],
                href="/cuestionario", active="exact"),                                    
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.NavLink([html.I(className="bi bi-file-person-fill ic"),"Sobre Nosotros"],
                href="/", active="exact"),  
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.NavLink([html.I(className="bi bi-shield-fill ic"),"Política de privacidad" ],
                href="/heatmaps", active="exact"),  
            ],
            vertical=True,
            pills=True,
            className="sidebar"
        ),
    ],
    
)

footer = html.Footer([
    html.Hr(),
    html.Div("Copyright ® Saby 2022 Aviso Legal & Política de Privacidad")
    ],
    className="content")

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        sidebar,
        dl.plugins.page_container,
        footer
        
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)


# This call will be used with Gunicorn server
#server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(debug=True)
