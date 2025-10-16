# 集合 (set): 无序、不重复
# 用途：去重、成员测试、数学集合操作（交集、并集等）。

fruits : set[str] = {"apple","banana","orange","apple"}
print(f"水果集合: {fruits}")
if "apple" in fruits:
    print("apple is in the set")
another_fruits: set[str] = {"apple","banana","pear"}

print(f"交集：{fruits.intersection(another_fruits)}")
print(f"并集:{fruits.union(another_fruits)}")