# 字典 (dict): 无序、可变，键值对
# 用途：存储键值对数据，就像电话簿一样，通过键快速查找值。
user_info : dict[str, str] = {
    "name":"Kitty",
    "age":24,
    "city":"Shanghai"
}

print(user_info)

user_info["age"] = 26
user_info["accupation"] = "Singer"
print(user_info)