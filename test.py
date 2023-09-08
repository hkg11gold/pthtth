import urllib.request
import json

# Tạo yêu cầu HTTP sử dụng urllib.request
url = 'https://api.github.com/users/hkg11gold/repos'
response = urllib.request.urlopen(url)

# Đọc dữ liệu từ phản hồi
data = json.load(response)

# In dữ liệu
print(data)

print("hello world")