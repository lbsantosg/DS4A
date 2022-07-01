def match_maker(COLE_COD_MCPIO_UBICACION,COLE_CALENDARIO,COLE_JORNADA,ESTU_GENERO,FAMI_TIENECOMPUTADOR,FAMI_TIENEINTERNET,FAMI_ESTRATOVIVIENDA,FAMI_CUARTOSHOGAR,FAMI_PERSONASHOGAR,FAMI_EDUCACIONPADRE,FAMI_EDUCACIONMADRE,FAMI_TRABAJOLABORPADRE,FAMI_TRABAJOLABORMADRE,Sociales,Naturales,Matematicas,Lectura,Ingles):
    return [{'name':f'fakeSchool{i}', 'id': i }for i in range(0,10)]

def get_school(schoolId):
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
