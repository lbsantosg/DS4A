from functions import * 
import pandas as pd 
clean_school = [] #read from csv 

def match_maker( **web_input ):
    '''
    1. Mapear inputs front => input modelos
    2. Cargar el modelo y hacer la prediccion
    3. Generar la huella del estudiante
    4. Filtrar colegios (huella)
    5. Match -> euclidean distance normalizada 
    6. Retornar top n 
    '''
    print(f'\n********Answers from the user in the webform************:\n {web_input}\n\n')
    model_input, parents_perception = map_inputs(**web_input)
    print(f'********Data transformed to be used by the model************:\n {model_input}\n\n')
    print(f'********Data of the parents perception:************\n {parents_perception}\n\n')
    score_predictions = get_predictions(model_input)
    print(f'********Predicted students score:************\n {score_predictions}\n\n')
    student_print = get_student_print(score_predictions, parents_perception )
    print(f'********Calculated student print:************\n {student_print}\n\n')
    ranked_print = get_rank(student_print)
    print(f'********Calculated ranked print:************\n {ranked_print}\n\n')
    top_schools = match(ranked_print, model_input['COLE_COD_MCPIO_UBICACION'], model_input['COLE_CALENDARIO'], model_input['COLE_JORNADA'])
    return top_schools

def get_school(schoolId):
    '''
    1. Filtrar colegio por id
    2. Retornar detalles del colegio 
    '''
    return filter_school(schoolId)

# TEST API
mock_input = {
    'dep_name': 'Antioquia',
    'mun_name' : 'Medellín',
    'school_calendar': 'A', 
    'school_shift': 'COMPLETA_UNICA', 
    'student_gender': 'OTRO', 
    'has_pc': 'Si', 
    'has_internet': 'Si',
    'economic_stratus': 'Estrato 6' ,
    'rooms_house': 'Dos',
    'family_members': '3 a 4', 
    'father_education': 'Educación profesional completa',
    'mother_education': 'Postgrado',
    'father_job': 'Pensionado', 
    'mother_job': 'Es agricultor, pesquero o jornalero', 
    'perception_socials': 3,
    'perception_science': 5,
    'perception_math': 5, 
    'perception_reading': 4,
    'perception_english': 3
}
top_schools = match_maker(**mock_input)
print (pd.DataFrame(top_schools))
print(get_school(305001014248))
