from math import dist
import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

# Load dataframes
divipola  = pd.read_csv("src/data/Divipola.csv", engine='python', sep = ';').set_index(['Departamento','Municipio'])
Edu       = pd.read_csv("src/data/Edu.csv", engine='python', sep = ';')
Labor     = pd.read_csv("src/data/Labor.csv", engine='python', sep = ';')
all_schools = pd.read_csv("src/data/final_schools.csv", engine='python', sep = ',')

# Load Model Coefficients
B_PUNT_GLOBAL = pd.read_csv("src/data/B_PUNT_GLOBAL.csv", engine='python', sep = ',')
B_PUNT_SOC    = pd.read_csv("src/data/B_PUNT_SOC.csv", engine='python', sep = ',')
B_PUNT_C_NAT  = pd.read_csv("src/data/B_PUNT_C_NAT.csv", engine='python', sep = ',')
B_PUNT_MAT    = pd.read_csv("src/data/B_PUNT_MAT.csv", engine='python', sep = ',')
B_PUNT_LECT   = pd.read_csv("src/data/B_PUNT_LECT.csv", engine='python', sep = ',')
B_PUNT_ING    = pd.read_csv("src/data/B_PUNT_ING.csv", engine='python', sep = ',')    

# Load Max/Min school records
Punt_MinMax    = pd.read_csv("src/data/Punt_MinMax.csv", engine='python', sep = ',')

def filter_school(id): 
    school = all_schools[all_schools['COLE_COD_DANE_ESTABLECIMIENTO'] == int(id)]
    return school

def map_inputs(  
    dep_name, 
    mun_name, 
    school_calendar,  
    school_shift, 
    student_gender,
    has_pc, 
    has_internet,
    economic_stratus,
    rooms_house,
    family_members, 
    father_education,
    father_job, 
    mother_education,
    mother_job, 
    perception_socials,
    perception_science,
    perception_math, 
    perception_reading,
    perception_english
    ):
    '''
    params: 
        - All fields from the web form 
    returns: 
        - List with all values needed to make prediction
        - Dict with category preferences 
    '''
    # Map department/municipality name to municipality code, use divipola dataframe
    mun_code = str(divipola.sort_index().loc[(dep_name,mun_name),'Munpio_Cod1'].values[0])

    # Set default gender 
    student_gender = 'M' if student_gender == 'OTRO' else student_gender

    # Get Max education level 
    parents_education = get_max_edu(edu_mother= mother_education, edu_father= father_education)
    parents_job = get_max_job(job_mother= mother_job, job_father= father_job) 

    # Get PC - Internet interaction
    pc_internet_interaction = np.nan if has_pc == 'Si' and has_internet == 'Si' else 0
    return { 
        'COLE_COD_MCPIO_UBICACION': mun_code, 
        'COLE_CALENDARIO': school_calendar,
        'COLE_JORNADA' : school_shift,
        'ESTU_GENERO': student_gender,
        'FAMI_TIENECOMPUTADOR' : has_pc,
        'FAMI_TIENEINTERNET': has_internet,
        'FAMI_ESTRATOVIVIENDA' : economic_stratus,
        'FAMI_CUARTOSHOGAR': rooms_house,
        'FAMI_PERSONASHOGAR': family_members,
        'FAMI_EDUCACIONPADRE': father_education,
        'FAMI_EDUCACIONMADRE': mother_education,
        'FAMI_TRABAJOLABORPADRE': father_job,
        'FAMI_TRABAJOLABORMADRE': mother_job,
        'Padres_Edu': parents_education,
        'Padres_Labor': parents_job,
        'Interaccion_Computador_Internet': pc_internet_interaction
    },{
        'socials': perception_socials,
        'science': perception_science,
        'math': perception_math,
        'reading': perception_reading,
        'english': perception_english
    }

def get_predictions(model_input):
    '''
    params: 
        - Model input list
    returns: 
        - List with all values needed to make prediction
        - dict with predicted scores where:
            key => area (math, science, ...)
            value => predicted score for that area
    '''
    predicted_scores = {}
    all_models = [B_PUNT_SOC, B_PUNT_C_NAT, B_PUNT_MAT, B_PUNT_LECT, B_PUNT_ING]
    models_names = ["socials", "science", "math", "reading", "english"]
    for model, model_name in zip(all_models,models_names):
        prediction = get_prediction(model_input=model_input, enfoque = model)
        predicted_scores[model_name] = prediction
    return predicted_scores

def get_prediction(model_input,enfoque):
    """
    Calcula la proyección por estudiante por enfoque
    
    Arguments:
    `Enfoque`: Betas Modelo Calculado de enfoque
    
    Output:
    `PROY_PUNT_F`: Puntaje proyectado estudiante dadas las caracteristicas
    """
    PROY_PUNT_F   = pd.DataFrame.from_dict(model_input, orient='index').reset_index()
    PROY_PUNT_F.rename(columns = {'index': 'Variable', 0: 'Nivel'}, inplace=True)
    PROY_PUNT     = PROY_PUNT_F.merge(enfoque, on=["Variable","Nivel"], suffixes=(False, False))
    PROY_PUNT     = PROY_PUNT[PROY_PUNT["PValue"]<0.05]
    Intercepto    = pd.DataFrame({"Variable":["Intercepto"],"Coefficient":[enfoque.at[0,"Coefficient"]],"PValue":[enfoque.at[0,"PValue"]]})
    PROY_PUNT     = PROY_PUNT.append(Intercepto, ignore_index=True)
    PROY_PUNT_F   = np.exp((PROY_PUNT["Coefficient"].sum()))    
    return PROY_PUNT_F

def get_student_print(predicted_scores, parents_perception ):
    '''
    params: 
        - dict with predicted scores where:
            key => area (math, science, ...)
            value => predicted score for the area
        - dict with parent's perceptions where:
            key => area (math, science, ...)
            value => parent perception value       
    returns: 
        - students print dict 
            key => calculated importance value for that area
            value => area
    '''
    # Normalize parents perception
    normalized_perception = {}
    for area in parents_perception: 
        normalized_perception[area] = (parents_perception[area]-1 / 4) + 1
    
    # Normalize model's predictions
    min_score =  {'socials': 17, 'science': 20, 'math': 15, 'reading': 21, 'english': 13}
    max_score =  {'socials': 88, 'science': 85, 'math': 90, 'reading': 85, 'english': 99}
    normalized_predictions = {}
    for area in predicted_scores: 
        normalized_predictions[area] = (predicted_scores[area] - min_score[area]) / \
                                        (max_score[area] - min_score[area]) + 1
    # Generate student's print
    student_print = {}
    for area in normalized_perception: 
        value = normalized_perception[area] * normalized_predictions[area]
        student_print[value] = area
    
    return student_print

def get_rank(student_print):
    '''
    params: 
        - students print dict 
            key => area (math, science, ...)
            value => parent perception value      
    returns: 
         - ranked print dict 
            key => area (math, science, ...)
            value => order (rank) of importance for that area 
    '''
    values = list(student_print.keys())
    values.sort(reverse=True)
    ranked_print = {}
    for idx in range(0,len(values)):
        area = student_print[values[idx]]
        ranked_print[area] = idx+1
        
    return ranked_print 

def get_euclidean_distance(school, student_vector, areas_data):
    '''
    params: 
        - School df 
        - Student's print vector
        - Names of the areas to the school vector can be created with the exact same order     
    returns: 
        - distance between vectors
    '''
    school_vector = [school[area] for area in areas_data]
    euclidean_distance = dist(student_vector, school_vector)
    return euclidean_distance

def calculate_score(school, max_distance, min_distance): 
    '''
    params: 
        - School df 
        - Max distance among all euclidean distances between school and student print
        - Min distance among all euclidean distances between school and student print     
    returns: 
        - Calculated score - this is the value that defines the likeability of the school 
    '''
    distance_norm = (max_distance - school['euclidean_distance']) / max(0.0000001,(max_distance - min_distance)) + 1
    score = distance_norm * school['PUNT_GLOBAL']
    return score 

def match(students_print, mun, cal, shift):
    '''
    params: 
        - ranked student's print dict 
            key => area (math, science, ...)
            value => order (rank) of importance for that area 
        - Municipality code id
        - School Calendar 
        - School shift   
    returns: 
        - DF of the top 10 schools
    '''
    # FILTER SCHOOLS BY MUN, CAL, SHIFT
    filtered_schools = all_schools[all_schools['COLE_COD_MCPIO_UBICACION'] == int(mun)] 
    filtered_schools = filtered_schools[filtered_schools['COLE_CALENDARIO'] == cal]
    filtered_schools = filtered_schools[filtered_schools['COLE_JORNADA'] == shift]

    # GET EUCLIDEAN DISTANCE BETWEEN STUDENT'S PRINT AND SCHOOLS
    areas = ('socials', 'science', 'math', 'reading', 'english')
    areas_data =('sociales_ciudanas_rank',
                'c_naturales_rank',
                'matematicas_rank',   
                'lectura_critica_rank',             
                'ingles_rank')
    student_vector = [students_print[area] for area in areas]

    filtered_schools['euclidean_distance'] = filtered_schools.apply(lambda x : get_euclidean_distance(x, student_vector, areas_data), axis=1)
    max_distance = filtered_schools['euclidean_distance'].max()
    min_distance = filtered_schools['euclidean_distance'].min()

    # NORMALIZE EUCLIDEAN DISTANCES 
    filtered_schools['calculated_score'] = filtered_schools.apply(lambda x : calculate_score(x,max_distance=max_distance, min_distance=min_distance), axis=1)

    # SORT SCHOOLS 
    filtered_schools.sort_values(by= ['calculated_score', 'PUNT_GLOBAL'], ascending=False, inplace=True)
    return filtered_schools[['COLE_COD_DANE_ESTABLECIMIENTO', 'COLE_NOMBRE_SEDE','euclidean_distance','calculated_score']].head(10)

def get_max_edu(edu_mother, edu_father): 
    '''
    params: 
        - edu_mother : string of mother education as came from the web form    
        - edu_father : string of mother education as came from the web form  
    returns: 
        - parent_education: education level with higher weight
    '''
    father_index  = Edu.set_index('Edu').at[edu_father,'Edu_Indice']
    mother_index  = Edu.set_index('Edu').at[edu_mother,'Edu_Indice']
    parents_education = Edu.set_index('Edu_Indice').at[max(father_index, mother_index),'Edu']
 
    return parents_education

def get_max_job(job_mother, job_father): 
    '''
    params: 
        - job_mother : string of mother job as came from the web form    
        - job_father : string of mother job as came from the web form  
    returns: 
        - parent_job : job level with higher weight
    '''
    father_index  = Labor.set_index('Labor').at[job_father,'Labor_Indice']
    mother_index  = Labor.set_index('Labor').at[job_mother,'Labor_Indice']
    parents_job   = Labor.set_index('Labor_Indice').at[max(father_index, mother_index),'Labor']

    return parents_job


