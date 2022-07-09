import dash
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import json


register_page(__name__, path="/")



layout=  dbc.Container([
   dbc.Row([
    dbc.Col(html.H1("Bienvenido a"),className="col_one"),
    dbc.Col(html.Img(src="./assets/images/saby_logo.png"),className="col_two")

   ],className="content tcenter"   
   ) 

])
