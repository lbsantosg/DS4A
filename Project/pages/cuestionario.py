#Importing libraries
from gc import callbacks
from dash import html , dcc, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import dash_trich_components as dtc
import json
from dash import Input, Output

#Importing components
from components.drop_text.dropt import dropt
from components.slider.slider import slider
from components.rbutton.rbutton import rbutton

#Registering page path
register_page(__name__, path="/cuestionario")

#Getting json data and definig data variables
j = open("./data/jsonfiles/demo.json")
datastore=  json.load(j)
options= list(datastore["demo_options"])

#Defining constants
radioClass= "radio-group tcenter"

#Defining our data variable
respuestas=[]

#Defining multiple forms type for each question
ciudad= html.Div([
                dbc.Label("Por favor seleccione el departamento y municipio de interés: "),
                html.Br(),
                html.Br(),
                dcc.Dropdown(options, placeholder='Seleccione el departamento', id='input_departamento', className="drop"),
                html.Br(),
                dcc.Dropdown(options, placeholder='Seleccione la ciudad', id='input_ciudad', className="drop"),
                html.Br(),
                html.Br(),
                html.Br(),
            ]
            ,className="tcenter"
                    
        )                        

calendario= html.Div([
                dbc.Label("Por favor seleccione el calendario de su interés:"),
                html.Br(),
                html.Br(),
                rbutton("iCalendario", {"Calendario A": "a", "Calendario B" : "b"}).display()      
                ],
                className= radioClass                                             
            )
            
jornada= html.Div([
                dbc.Label("Por favor seleccione la jornada de su interes: "),
                html.Br(),
                html.Br(),
                rbutton("iJornada", {"Mañana": "mañana", "Tarde" : "tarde", "Completa": "completa"}).display()      
                ],
                className= radioClass                          
            )

genero= html.Div([
                dbc.Label("Por favor seleccione el género de colegio de su interés: "),
                html.Br(),
                html.Br(),
                rbutton("iGenero", {"Masculino": "m", "Femenino" : "f", "Mixto": "mix"}).display()      
                ],
                className=radioClass                           
            )  

computador= html.Div([
                dbc.Label("¿En su núcleo familiar, el estudiante tiene acceso a un computador para estudios?"),
                html.Br(),
                html.Br(),
                rbutton("iComputador", {"Si": "si", "No" : "no"}).display()           
                ],
                className=radioClass                          
            )  

internet= html.Div([
                dbc.Label("¿En su núcleo familiar, el estudiante tiene acceso a internet para estudios?"),
                html.Br(),
                html.Br(),
                rbutton("iInternet", {"Si": "si", "No" : "no"}).display()         
            ],
                className="radio-group tcenter"                           
            )  

estrato= html.Div([
                dbc.Label("¿A cuál estrato pertenece la vivienda de su núcleo familiar?"),
                html.Br(),
                html.Br(),
                rbutton("iComputador", {"Estrato 1": 1, "Estrato 2" : 2, "Estarto 3 ": 3, "Estrato 4": 4, "Estrato 5": 5, "Estrato 6" : 6}).display()         
                ],
                className=radioClass                          
            )              

cuartos= html.Div([
                dbc.Label("¿Cuántas habitaciones hay en su vivienda?"),
                html.Br(),
                html.Br(),
                dbc.Input(type="number", min=1, max=20, step=1, id="styled-numeric-input iCuartos"),                           
            ], className="tcenter" ) 

personas= html.Div([
                dbc.Label("¿Aparte del estudiante, cuántas personas hay en su núcleo familiar?"),
                html.Br(),
                html.Br(),
                dbc.Input(type="number", min=1, max=20, step=1, id="styled-numeric-input iPersonas"),                            
            ], className="tcenter") 

escolaridad= html.Div([
                dbc.Label("¿Cuál es el nivel máximo de escolaridad alcanzado por los padres del estudiante?"),
                html.Br(),
                html.Br(),
                dcc.Dropdown(options, placeholder='Escolaridad Padre', id='input_esco_padre', className="drop"),
                html.Br(),
                dcc.Dropdown(options, placeholder='Escolaridad Madre', id='input_esco_madre', className="drop"), 
                html.Br(),           
                html.Br(),
            ],className="tcenter") 

ocupacion= html.Div([
                dbc.Label("¿A qué categoría pertenece la labor u ocupación de los padres del estudiante?"),
                html.Br(),
                html.Br(),
                dcc.Dropdown(options, placeholder='Categoría Ocupacion', id='input_ocupación', className="drop"),
                html.Br(),
                html.Br()                         
            ],className="tcenter")
                                         
sociales= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las ciencias sociales?"),
                html.Br(),
                html.Br(),
                slider("vsociales",1,5,1).display()                          
            ], className="tcenter")     

naturales= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las ciencias naturales?"),
                html.Br(),
                html.Br(),
                slider("vnaturales",1,5,1).display()                          
            ], className="tcenter")     

matematicas= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las matemáticas?"),
                html.Br(),
                html.Br(),
                slider("vmatematicas",1,5,1).display()                            
            ], className="tcenter")                

lectura= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con la lectura?") ,
                html.Br(),
                html.Br(),
                slider("vlectura",1,5,1).display()                            
            ], className="tcenter")     

ingles= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con el idioma inglés?"),
                html.Br(),
                html.Br(),
                slider("vingles",1,5,1).display()                            
            ], className="tcenter")             

#Establishing carousel with questions
carousel = dtc.Carousel([
            ciudad,
            calendario,
            jornada,
            genero,
            computador,
            internet,
            estrato,
            cuartos,
            personas,
            escolaridad,
            ocupacion,
            sociales,
            naturales,
            matematicas,
            lectura,
            ingles            
        ],            
        arrows= True,    
        infinite=False,
        slides_to_show=1,
        slides_to_scroll=1,
        swipe_to_slide=False,
        dots=True     
		)

#Establishing layout
layout= dbc.Container(
    [
        carousel
    ],
    className="dbc content",
    fluid=True,
)

#Establishing callbacks
@callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'