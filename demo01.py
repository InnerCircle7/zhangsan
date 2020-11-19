# 方法： print 打印  input 输入 type 读取数据的格式 str() int() 数据转换 len()计算数据的长度
"""
print("hello world")  # 字符串
print(2333)  # 整数
print(2.333)  # 浮点数
print(True)  # 布尔值
print(())  # 元组
print([])  # 列表
print({})  # 字典

hahahha

print("haha",2333,2.333)
print("haha"+"xixi")  # 字符串的拼接 同样的类型
print("haha"*50)
print(((1+2)*100-9.9)/2)
print(2>3)

name = "zhangsan"  # 把zhangsan这个值赋值给了名字叫name的这个变量
print(name)
"""


# 数据格式的转换
# c = type(2333)
# print(c)
# print(type("hello world"))  # 字符串
# print(type(2333))  # 整数
# print(type(2.333))  # 浮点数
# print(type(True))  # 布尔值
# print(type(()))  # 元组
# print(type([]))  # 列表
# print(type({}))  # 字典

a = int("2333")  # 字符串转整数
print(type(a))

#两种方法
# a = input("请输入：")
# b = input("请输入：")
# print("input获取的内容:",int(a)+int(b))

# a = float(input("请输入："))
# b = float(input("请输入："))
# print("input获取的内容:",a+b)

# a = "xixi"
# print(len(a))
"""
练习：通过代码获取两段内容，并且计算他们长度的和。123
"""
a = input("请输入内容：")
b = input("请输入内容：")
print(len(a+b))