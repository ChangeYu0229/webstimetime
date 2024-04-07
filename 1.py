import json

# 读取uptime.json文件
with open('uptime.json', 'r') as file:
    data = json.load(file)

# 每天增加1
data['uptime'] += 1

# 写入新的值
with open('uptime.json', 'w') as file:
    json.dump(data, file)
