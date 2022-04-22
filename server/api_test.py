from requests import get, delete, post

# регистрация нового пользователя
print(post('http://localhost:5000/api/user_verification/new_user', json={'name': 'Razvlekal0vka',
                                                                         'username': 'bezzubka',
                                                                         'password': 'mkdog59',
                                                                         'phone': '+7(866)-666-66-66',
                                                                         'email': '66@gmail.com',
                                                                         'activation_code': 'jjOCo2c$ZfgJ'}).json())

# докидка кода активации
print(post('http://localhost:5000/api/user_verification/adding_an_activation_code', json={'name': '',
                                                                                          'username': 'bezzubka',
                                                                                          'password': 'mkdog59',
                                                                                          'phone': '',
                                                                                          'email': '',
                                                                                          'activation_code': 'jjOCo2c$ZfgJ'}).json())

# может ли пользователь пользоваться сервисом
""""еще не работает"""
print(post('http://localhost:5000/api/user_verification/service_access', json={'name': '',
                                                                                          'username': 'bezzubka',
                                                                                          'password': 'mkdog59',
                                                                                          'phone': '',
                                                                                          'email': '',
                                                                                          'activation_code': ''}).json())

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
# account successfully created with activation code - аккаунт успешно зарегистрирован с кодом активации
# account successfully created without activation code - аккаунт успешно зарегистрирован без кода активации
# activation code is not active yet - этот код активации еще не активен
# activation code expired - этот код активации уже просрочен
# this code is already used in your account - это код уже используется в вашем аккаунте
# such code does not exist or is already being used by someone - такой код не существует или уже используется кем-то
# account successfully activated - аккаунт успешно активирован
