import dash_trich_components as dtc
from dash import html

content_1 = html.Div('content 1')
content_2 = html.Div('content 2')
content_3 = html.Div('content 3')
content_4 = html.Div('content 4')
content_5 = html.Div('content 5')

sidebar = html.Div([
    dtc.SideBar([
        dtc.SideBarItem(id='id_1', label="Label 1", icon="fas fa-home"),
        dtc.SideBarItem(id='id_2', label="Label 2", icon="fas fa-chart-line"),
        dtc.SideBarItem(id='id_3', label="Label 3", icon="far fa-list-alt"),
        dtc.SideBarItem(id='id_4', label="Label 4", icon="fas fa-info-circle"),
        dtc.SideBarItem(id='id_5', label="Label 5", icon="fas fa-cog"),
    ]),
    html.Div([
    ], id="page_content"),
])



