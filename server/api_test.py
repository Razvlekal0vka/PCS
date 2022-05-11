from requests import get, delete, post

# регистрация нового пользователя
print(post('http://127.0.0.1:8081/api/user_verification/new_user', json={'id': '',
                                                                         'name': 'Razvlekal0vka',
                                                                         'username': 'bezzubka',
                                                                         'password': 'mkdog59',
                                                                         'phone': '+7(666)-666-66-66',
                                                                         'email': '666@gmail.com',
                                                                         'activation_code': ''}).json())

# докидка кода активации
print(post('http://127.0.0.1:8081/api/user_verification/adding_an_activation_code', json={'id': '',
                                                                                          'name': '',
                                                                                          'username': 'bezzubka',
                                                                                          'password': 'mkdog59',
                                                                                          'phone': '',
                                                                                          'email': '',
                                                                                          'activation_code': 'P0ZWm%koI8A@'}).json())
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
# you are already using this activation code - вы уже используете этот код активации
# you are already using another activation code - вы уже используете другой код активации
# this user does not exist in the system - такого пользователя нет в системе
"""=================================================================================================================="""
# авторизация
print(post('http://127.0.0.1:8081/api/user_verification/account_login', json={'id': '',
                                                                              'name': '',
                                                                              'username': 'bezzubka',
                                                                              'password': 'mkdog59',
                                                                              'phone': '',
                                                                              'email': '',
                                                                              'activation_code': ''}).json())
# может вернуть True пользователя если авторизация прошла успешно
# the user does not exist or the data entered is incorrect - такого пользователя не существует или введены неправильные
# данные
"""=================================================================================================================="""
# что может делать пользователь
print(post('http://127.0.0.1:8081/api/user_verification/check_available_functions', json={'id': '',
                                                                                          'name': '',
                                                                                          'username': 'bezzubka',
                                                                                          'password': 'mkdog59',
                                                                                          'phone': '',
                                                                                          'email': '',
                                                                                          'activation_code': ''}).json())
# может вернуть True пользователя если ограничений нет
# the user does not exist or the data entered is incorrect - такого пользователя не существует или введены неправильные
# данные
"""=================================================================================================================="""
# запрос на добавление файла в документацию о файлах
print(post('http://127.0.0.1:8081/api/user_file/new_file', json={'username': 'bezzubka',
                                                                 'password': 'mkdog59',
                                                                 'friend_username': '',
                                                                 'new_file': 'xuy.txt',
                                                                 'delete_file': '',
                                                                 'email': '',
                                                                 'accessible_file': ''}).json())
# True - all good
# the user does not exist or the data entered is incorrect - такого пользователя не существует или введены неправильные
# данные
"""=================================================================================================================="""
# запрос на удаление файла в документацию о файлах
print(post('http://127.0.0.1:8081/api/user_file/delete_file', json={'username': 'bezzubka',
                                                                    'password': 'mkdog59',
                                                                    'friend_username': '',
                                                                    'new_file': '',
                                                                    'delete_file': 'xuy(1).txt',
                                                                    'email': '',
                                                                    'accessible_file': ''}).json())
# True - all good
# no_such_file_exists - такого файла не существует
# the user does not exist or the data entered is incorrect - такого пользователя не существует или введены неправильные
# данные
"""=================================================================================================================="""
# запрос на изменение имени или расположения файла в документацию о файлах
print(post('http://127.0.0.1:8081/api/user_file/change_file', json={'username': 'bezzubka',
                                                                    'password': 'mkdog59',
                                                                    'friend_username': '',
                                                                    'new_file': 'MyBadFile/GoodFile.txt',
                                                                    'delete_file': 'xuy(0).txt',
                                                                    'email': '',
                                                                    'accessible_file': ''}).json())
# True - all good
# no_such_file_exists - такого файла не существует
# the user does not exist or the data entered is incorrect - такого пользователя не существует или введены неправильные
# данные
"""=================================================================================================================="""
# получение id пользователя
print(post('http://127.0.0.1:8081/api/user_verification/user_id', json={'id': '',
                                                                        'name': '',
                                                                        'username': 'bezzubka',
                                                                        'password': 'mkdog59',
                                                                        'phone': '',
                                                                        'email': '',
                                                                        'activation_code': ''}).json())
# может вернуть id пользователя если авторизация прошла успешно
# the user does not exist or the data entered is incorrect - такого пользователя не существует или введены неправильные
# данные
"""=================================================================================================================="""
# связь teledram и PCS id
print(post('http://127.0.0.1:8081/api/telegram/telegram_id', json={'telegram_id': '',
                                                                   'pcs_id': ''}).json())
# True - all good
