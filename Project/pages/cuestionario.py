import dash
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import dash_trich_components as dtc



register_page(__name__, path="/cuestionario")

#Defining multiple forms type for each question

slider = html.Div(
    [        
        dcc.Slider(id="slider", min=1, max=5, step=1, value=3),
    ],
    className="mb-3 slider",
)

form_p= html.Div([
                dbc.Label("Email", html_for="example-email"),
                dbc.Input(type="email", id="example-email", placeholder="Enter email"),
                dbc.FormText(
                    "Are you on email? You simply have to be these days",
                    color="secondary"
                )                
            ])

ciudad= html.Div([
                dbc.Label("Por favor seleccione el departamento y municipio de interés: ")                           
            ])

calendario= html.Div([
                dbc.Label("Por favor seleccione el calendario de su interés: "),
                html.Br(),
                html.Br(),
                dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Calendario tipo A", "value": "a"},
                                {"label": "Calendario tipo B", "value": "b"},
                                
                            ],
                            value="a",
                        ),
                        
                    ],
                className="radio-group tcenter"                                               
            )
            
jornada= html.Div([
                dbc.Label("Por favor seleccione la jornada de su interes: "),
                html.Br(),
                html.Br(),
                dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Mañana", "value": "mañana"},
                                {"label": "Tarde", "value": "tarde"},
                                {"label": "Completa", "value": "completa"},
                            ],
                            value="completa",
                        ),
                        
                    ],
                className="radio-group tcenter"                           
            )

genero= html.Div([
                dbc.Label("Por favor seleccione el genero de colegio de su interés: "),
                html.Br(),
                html.Br(),
                dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Masculino", "value": "masculino"},
                                {"label": "Femenino", "value": "femenino"},
                                {"label": "Mixto", "value": "mixto"},
                            ],
                            value="mixto",
                        ),
                        
                    ],
                className="radio-group tcenter"                           
            )  

computador= html.Div([
                dbc.Label("¿En su núcleo familiar, el estudiante tiene acceso a un computador para estudios?"),
                html.Br(),
                html.Br(),
                dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Si", "value": True},
                                {"label": "No", "value": False},
                                
                            ],
                            value=True,
                        ),
                        
                    ],
                className="radio-group tcenter"                           
            )  

internet= html.Div([
                dbc.Label("¿En su núcleo familiar, el estudiante tiene acceso a internet para estudios?"),
                html.Br(),
                html.Br(),
                dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Si", "value": True},
                                {"label": "No", "value": False},
                                
                            ],
                            value=True,
                        ),
                        
                    ],
                className="radio-group tcenter"                           
            )  

estrato= html.Div([
                dbc.Label("¿A cuál estrato pertenece la vivienda de su núcleo familiar?"),
                html.Br(),
                html.Br(),
                dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Estrato 1", "value": 1},
                                {"label": "Estrato 2", "value": 2},
                                {"label": "Estrato 3", "value": 3},
                                {"label": "Estrato 4", "value": 4},
                                {"label": "Estrato 5", "value": 5},
                                {"label": "Estrato 6", "value": 6},
                                
                            ],
                            value=3,
                        ),
                        
                    ],
                className="radio-group tcenter"                           
            )              

cuartos= html.Div([
                dbc.Label("¿Cuántos cuartos hay en su vivienda?")                           
            ]) 

personas= html.Div([
                dbc.Label("¿Aparte del estudiante, cuántas personas hay en su núcleo familia?")                           
            ]) 

escolaridad= html.Div([
                dbc.Label("¿Cuál es el nivel máximo de escolaridad alcanzado por los padres del estudiante?")                           
            ]) 

ocupacion= html.Div([
                dbc.Label("¿A qué categoría pertenece la labor u ocupación de los padres del estudiante?")                           
            ])             

sociales= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las ciencias sociales?"),
                slider                         
            ])   

naturales= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las ciencias naturales?"),
                slider                          
            ])  

matematicas= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con las matemáticas?"),
                slider                          
            ])              

lectura= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con la lectura?") ,
                slider                          
            ]) 

ingles= html.Div([
                dbc.Label("En una escala de 1 a 5: ¿Cuál cree que es la afinidad de su hijo con el idioma inglés?"),
                slider                          
            ])             

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
        swipe_to_slide=False     
		)

layout= dbc.Container(
    [
        carousel
    ],
    className="dbc content",
    fluid=True,
)