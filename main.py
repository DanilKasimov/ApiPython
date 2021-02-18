import requests
t = '4274952bab18c8db9b'
token = 'ebfe6f90ebfe6f90ebfe6f9025eb880df1eebfeebfe6f908bdb5b9084c8fed66444812c'
version = 5.130
#https://oauth.vk.com/blank.html#code=4274952bab18c8db9b
#https://api.vk.com/method/messages.send?access_token=4274952bab18c8db9b&v=5.130&user_id=169104461&message=%22%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%22
response = requests.get('https://api.vk.com/method/messages.send?access_token=4274952bab18c8db9b&v=5.130&user_id=169104461&message=%22%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%22')