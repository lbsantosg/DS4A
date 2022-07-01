from functions import * 
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
    # top_schools = match_maker(student_print, clean_school[median_global]  )
    return [{'name':f'fakeSchool{i}', 'id': i }for i in range(0,10)]
    # return model_input, parents_perception

def get_school(schoolId):
    '''
    1. Filtrar colegio por id
    2. Retornar detalles del colegio 
    '''
    return {
        'name': 'fakeSchool1',
        'id': '1234',
        'email': 'mail@mail.com',
        'phone': '123456789',
        'math': {
            '2017': 24,
            '2018': 34,
            '2020': 50,
            '2021': 56
        },
        'reading': {
            '2017': 28,
            '2018': 38,
            '2020': 58,
            '2021': 58
        },
        'science': {
            '2017': 84,
            '2018': 84,
            '2020': 80,
            '2021': 86
        },
        'features': {
            'languages': ['ALEMAN','INGLES']
        }
    }

# TEST API
mock_input = {
    'mun_name' : 'Bogotá, D.C.',
    'school_calendar': 'B', 
    'school_shift': 'COMPLETA_UNICA', 
    'student_gender': 'F', 
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
test = match_maker(**mock_input)