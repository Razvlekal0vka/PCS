# связь teledram и PCS id
from requests import get, delete, post
print(post('http://127.0.0.1:8081/api/telegram/telegram_id', json={'telegram_id': '666',
                                                                   'pcs_id': '6'}).json())
# True - all good