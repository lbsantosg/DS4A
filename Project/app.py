#libraries
from pydoc import classname
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
from dash import Input, Output, dcc, html
import dash_trich_components as dtc



# Dash instance declaration , using icons from font awesome
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[
{
    'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    'crossorigin': 'anonymous'
}
],)

#Top navbar
navbar = dbc.NavbarSimple(
    [html.A([
        html.Img(src="./assets/images/logo.png", height="52px")
    ],
    href="/"      
        
    )],
    dark=True,
    class_name="",
    sticky="top",
)

#Creating sidebar, to insert content on page use className : content
sidebar =  html.Div([
    dtc.SideBar([
        dtc.SideBarItem(id='id_1', label="Hacer Test", icon="fas fa-home"),
        dtc.SideBarItem(id='id_2', label="Sobre Nosotros", icon="fas fa-chart-line"),
        dtc.SideBarItem(id='id_3', label="Política de Uso", icon="far fa-list-alt"),
    ]),
    html.Div([
    ], 
    id="page_content",
    ),
])


#Main layout
app.layout = dbc.Container(
    [
        navbar,
        sidebar,
        dl.plugins.page_container,
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
