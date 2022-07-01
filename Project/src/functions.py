import numpy as np
import statsmodels.api as sm
import random
def map_inputs(    
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
    # Map municipality name to municipality code, use divipola dict
    divipola = {
        'Bogotá, D.C.': 11001
        # TODO: add missing codes
    }
    mun_code = divipola[mun_name]

    # Get Max education level 
    parents_education = get_max_edu(edu_mother= mother_education, edu_father= father_education)
    parents_job = get_max_job(job_mother= mother_job, job_father= father_job) 

    # Get PC - Internet interaction
    # TODO: Ask Andres how to make the interaction
    pc_internet_interaction = np.nan if has_pc and has_internet else np.nan
    return (    
        mun_code, 
        school_calendar,
        school_shift,
        student_gender,
        has_pc,
        has_internet,
        economic_stratus,
        rooms_house,
        family_members,
        father_education,
        mother_education,
        father_job,
        mother_job,
        parents_education,
        parents_job,
        pc_internet_interaction
    ),{
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
    for model in ["socials_model", "science_model", "math_model", "reading_model", "english_model"]:
        # model = sm.load(model)
        # prediction = model.predict(model_input)
        prediction = random.randint(50,90)
        key = model.split("_")[0]
        predicted_scores[key] = prediction
    return predicted_scores

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
            key => area (math, science, ...)
            value => parent perception value  
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
        student_print[area] = normalized_perception[area] * normalized_predictions[area]
    
    return student_print 

def match_maker(students_print, school_normalized_median):
    '''
    1. Get Euclidean distance between vectors
    2. Normalize distances with rank instead of values
    3. Normalize school global scores 
    4. Sort results (sort by distance, then by school score)
    '''
    top_schools = [111,112,113,114]
    return top_schools

def get_max_edu(edu_mother, edu_father): 
    #TODO: calculate max educational level
    return edu_mother

def get_max_job(job_mother, job_father): 
    #TODO: calculate max educational level
    return job_father