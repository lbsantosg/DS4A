import dash
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import json


#Getting json info
j = open("./data/jsonfiles/demo.json")
datastore=  json.load(j)
options= datastore["demo_options"]

register_page(__name__, path="/")



layout=  dbc.DropdownMenu(
    
    [        
        dbc.DropdownMenuItem(option)
        for option in options
    ],
    label = "Test Menu",
    menu_variant="dark",
    className="content"
    
)