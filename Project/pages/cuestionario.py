#Importing libraries
from this import d
from dash import html , dcc, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import dash_trich_components as dtc
import json
from dash import Input, Output, State
from sqlalchemy import null

#Importing components
from components.drop_text.dropt import dropt
from components.slider.slider import slider
from components.rbutton.rbutton import rbutton

#Importing local API functions
from src.api import match_maker, get_school

#Registering page path
register_page(__name__, path="/cuestionario")

#Getting json data and definig data variables
j = open("./data/jsonfiles/demo.json")
datastore=  json.load(j)
options= datastore["demo_options"]

f= open("./data/jsonfiles/fields.json")
fields= json.load(f)


#Defining constants
radioClass= "radio-group tcenter"

#Defining our data variable
respuestas={'dep_name': 'Antioquia','mun_name': 'Bogotá, D.C.', 'school_calendar': 'B', 'school_shift': 'COMPLETA_UNICA',
 'student_gender': 'F', 'has_pc': 'Si', 'has_internet': 'Si', 'economic_stratus': 'Estrato 6',
  'rooms_house': 'Dos', 'family_members': '3 a 4', 'father_education': 'Educación profesional completa',
   'mother_education': 'Postgrado', 'father_job': 'Pensionado', 'mother_job': 'Es agricultor, pesquero o jornalero',
    'perception_socials': 3, 'perception_science': 5, 'perception_math': 5,
     'perception_reading': 4, 'perception_english': 3}

#Defining multiple forms type for each question
ciudad= html.Div([
                dbc.Label("Por favor seleccione el departamento y municipio de interés: "),
                html.Br(),
                html.Br(),
                dcc.Dropdown(options=list(options), placeholder='Seleccione el departamento', id='input_departamento', className="drop"),
                html.Br(),
                dcc.Dropdown(options=list(options), placeholder='Seleccione la ciudad', id='input_ciudad', className="drop", disabled=True),
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
                rbutton("input_calendario", {"Calendario A": "a", "Calendario B" : "b"}).display()      
                ],
                className= radioClass                                             
            )
            
jornada= html.Div([
                dbc.Label("Por favor seleccione la jornada de su interes: "),
                html.Br(),
                html.Br(),
                rbutton("input_jornada", {"Mañana": "mañana", "Tarde" : "tarde", "Completa": "Completa_Unica"}).display()      
                ],
                className= radioClass                          
            )

genero= html.Div([
                dbc.Label("Por favor seleccione el género de colegio de su interés: "),
                html.Br(),
                html.Br(),
                rbutton("input_genero", {"Masculino": "M", "Femenino" : "F"}).display()      
                ],
                className=radioClass                           
            )  

computador= html.Div([
                dbc.Label("¿En su núcleo familiar, el estudiante tiene acceso a un computador para estudios?"),
                html.Br(),
                html.Br(),
                rbutton("input_computador", {"Si": "Si", "No" : "No"}).display()           
                ],
                className=radioClass                          
            )  

internet= html.Div([
                dbc.Label("¿En su núcleo familiar, el estudiante tiene acceso a internet para estudios?"),
                html.Br(),
                html.Br(),
                rbutton("input_internet", {"Si": "Si", "No" : "No"}).display()         
            ],
                className="radio-group tcenter"                           
            )  

estrato= html.Div([
                dbc.Label("¿A cuál estrato pertenece la vivienda de su núcleo familiar?"),
                html.Br(),
                html.Br(),
                rbutton("input_estrato", fields["FAMI_ESTRATOVIVIENDA"]).display()         
                ],
                className=radioClass                          
            )              

cuartos= html.Div([
                dbc.Label("¿Cuántas habitaciones hay en su vivienda?"),
                html.Br(),
                html.Br(),
               rbutton("input_cuartos", fields["FAMI_CUARTOSHOGAR"]).display()   ,                           
            ], className="tcenter" ) 

personas= html.Div([
                dbc.Label("¿Aparte del estudiante, cuántas personas hay en su núcleo familiar?"),
                html.Br(),
                html.Br(),
               rbutton("input_personas", fields["FAMI_PERSONASHOGAR"]).display(),                            
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
                dcc.Dropdown(options, placeholder='Categoría Ocupacion Padre', id='input_ocu_padre', className="drop"),
                html.Br(),
                dcc.Dropdown(options, placeholder='Categoría Ocupacion Madre', id='input_ocu_madre', className="drop"),
                html.Br()                         
            ],className="tcenter")
                                         
sociales= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las ciencias sociales?"),
                html.Br(),
                html.Br(),
                slider("input_sociales",1,5,1).display()                          
            ], className="tcenter")     

naturales= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las ciencias naturales?"),
                html.Br(),
                html.Br(),
                slider("input_naturales",1,5,1).display()                          
            ], className="tcenter")     

matematicas= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las matemáticas?"),
                html.Br(),
                html.Br(),
                slider("input_matematicas",1,5,1).display()                            
            ], className="tcenter")                

lectura= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con la lectura?") ,
                html.Br(),
                html.Br(),
                slider("input_lectura",1,5,1).display()                            
            ], className="tcenter")     

ingles= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con el idioma inglés?"),
                html.Br(),
                html.Br(),
                slider("input_ingles",1,5,1).display()                            
            ], className="tcenter")             

reserva= html.Div(id="reserva",hidden=True)

modal= dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Resultados"),class_name="mheader"),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Cerrar", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            className='modal-lg',
            is_open=False,
        )

calcular= html.Div([
    reserva,
    modal,
    dbc.Button(
        "Calcular Resultados",
        id="calcular",        
    )
],className="tcenter")




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
            ingles,
            calcular            
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

#**Establishing callbacks**

#Changing city dropdown options when selecting department
@callback(
    [Output('input_ciudad', 'disabled'),
    Output('input_ciudad', 'options')],
    [Input('input_departamento', 'value')]
)
def update_output(value):

    if value == 'Seleccione el departamento' or value == "" or value == None:
        return [True, list(options)]
    else:
        return [False, options[value]]

#--Adding  user inputs into answers variable--

@callback(
    Output('reserva','children'),
    [
    Input('input_departamento', 'value'),
    Input('input_ciudad', 'value'),
    Input('input_calendario', 'value'),
    Input('input_jornada', 'value'),
    Input('input_genero', 'value'),
    Input('input_computador', 'value'),
    Input('input_internet', 'value'),
    Input('input_estrato', 'value'),
    Input('input_cuartos', 'value'),
    Input('input_personas', 'value'),
    Input('input_esco_padre', 'value'),
    Input('input_esco_madre', 'value'),
    Input('input_ocu_padre', 'value'),
    Input('input_ocu_madre', 'value'),
    Input('input_sociales', 'value'),
    Input('input_naturales', 'value'),
    Input('input_matematicas', 'value'),
    Input('input_lectura', 'value'),
    Input('input_ingles', 'value'),

    ]
)
def change_data(departamento,ciudad,calendario,jornada,genero,computador,internet,estrato,cuartos,personas,esco_padre,esco_madre,ocu_padre,ocu_madre,sociales,naturales,matematicas,lectura,ingles):

        respuestas['dep_name']= departamento
        respuestas['mun_name'] = ciudad
        respuestas['school_calendar'] = calendario
        respuestas['school_shift'] = jornada
        respuestas['student_gender'] = genero
        respuestas['has_pc'] = computador
        respuestas['has_internet'] = internet
        respuestas['economic_stratus'] = estrato
        respuestas['rooms_house'] = cuartos
        respuestas['family_members'] = personas
        respuestas['father_education'] = esco_padre
        respuestas['mother_education'] = esco_madre
        respuestas['father_job'] = ocu_padre
        respuestas['mother_job'] = ocu_madre
        respuestas['perception_socials'] = sociales
        respuestas['perception_science'] = naturales
        respuestas['perception_math'] = matematicas
        respuestas['perception_reading'] = lectura
        respuestas['perception_english'] = ingles

        return str(respuestas)


#Creating button callback to print results:
@callback(
    Output('reserva','hidden'),
    Input('calcular', 'n_clicks'),

)
def calculate_print(btn):
    print(match_maker(respuestas))
    return True

    
@callback(
    Output("modal", "is_open"),
    [Input("calcular", "n_clicks"), Input("close", "n_clicks")] ,
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open