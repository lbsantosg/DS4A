import dash
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
#from components.kpi.kpibadge import kpibadge
#from components.maps.mapsample import mapsample
#mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

register_page(__name__, path="/")



layout=  dbc.DropdownMenu(
    label = "Test Menu",
    children= [
        
        dbc.DropdownMenuItem("Item 1"),
        dbc.DropdownMenuItem("Item 2"),
        dbc.DropdownMenuItem("Item 3"),

    ]
    
)