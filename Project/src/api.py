def match_maker():
    return [{'name':f'fakeSchool{i}', 'id': i }for i in range(0,10)]

def get_school():
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
