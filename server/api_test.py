from requests import get, delete, post

# print(get('http://localhost:5000/api/v2/users').json())

# wrong keys
print(post('http://localhost:5000/api/user_verification/new_user', json={'team_leader': 1,
                                                                         'work_size': 10,
                                                                         'collaborators': 'collaborators1',
                                                                         'is_finished': False}).json())

# print(post('http://localhost:5000/api/v2/users', json={'name': 'Oleg',
# 'surname': 'Zhdanov',
# 'age': 18,
# 'position': "student",
# 'speciality': "student",
# 'address': 'moscow',
# 'email': 'helge2003@yandex.ru',
# 'hashed_password': 'asd12easdsdf1112'}).json())
# print(get('http://localhost:5000/api/v2/users/7').json())
# print(delete('http://localhost:5000/api/v2/users/7').json())
# wrong id
# print(delete('http://localhost:5000/api/v2/users/777').json())
# print(get('http://localhost:5000/api/v2/users').json())
