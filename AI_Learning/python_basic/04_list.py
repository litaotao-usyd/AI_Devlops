# 列表 (list): 有序、可变
# 用途：存储一系列可以改变的数据，比如待办事项、商品列表。
tasks : list[str] = ["写代码","开会","看书"]
print(f"origin list:{tasks}")
tasks.append("运动")
tasks.remove("写代码")
print(f"new list:{tasks}")
print(f"first element:{tasks[0]}")