#libraries
from pydoc import classname
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
from dash import Input, Output, dcc, html
import dash_trich_components as dtc



# Dash instance declaration , using icons from font awesome
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.icons.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'], suppress_callback_exceptions=True)

#Top navbar
navbar= dbc.Navbar(
    dbc.Container(
        [
             html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="./assets/images/logo.png", height="52px")),
                    ],
                    className="navbar",
                ),
                href="/"
            ),
        ]
    ),
    sticky="top"
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
                dbc.NavLink([html.I(className="bi bi-house-fill ic")," Realizar Test"],
                href="/cuestionario", active="exact"),                                    
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.NavLink([html.I(className="bi bi-file-person-fill ic")," Sobre Nosotros"],
                href="/", active="exact"),  
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.NavLink([html.I(className="bi bi-shield-fill ic")," Política de privacidad" ],
                href="/politica_privacidad", active="exact"),  
            ],
            vertical=True,
            pills=True,
            className="sidebar"
        ),
    ],
    
)

footer = html.Footer([
    html.Hr(),
    html.Div(
        ["Copyright Saby ® 2022 - ",
         html.A("Política de Privacidad", href="/politica_privacidad")] ,
          style={"text-align" : "center"})
    ],
    className="footer")

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
