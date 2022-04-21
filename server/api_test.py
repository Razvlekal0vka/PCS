from requests import get, delete, post

# регистрация нового пользователя
print(post('http://localhost:5000/api/user_verification/new_user', json={'name': 'Razvlekal0vka',
                                                                         'username': 'bezzubka',
                                                                         'password': 'mkdog59',
                                                                         'phone': '+7(866)-666-66-66',
                                                                         'email': '66@gmail.com',
                                                                         'activation_code': 'jjOCo2c$ZfgJ'}).json())
# this login is already taken - этот логин уже кем-то занят
# this phone has already been used during registration - этот телефон уже использовался при регистрации
# this email address was already used during registration - эта почта уже использовалась при регистрации
# this activation code has already been used during registration
# invalid characters in name - недопустимое имя
# invalid name length - недопустимая длина имени
# invalid characters in username - недопустимый логин
# invalid username length - недопустимая длина логина
# invalid characters in password - недопустимый пароль
# invalid username password - недопустимая длина пароля
# account created successfully - аккаунт успешно зарегистрирован
# account created successfully - аккаунт успешно зарегистрирован

"""=================================================================================================================="""
