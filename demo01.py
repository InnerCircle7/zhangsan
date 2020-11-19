# 方法： print 打印  input 输入 type 读取数据的格式 str() int() 数据转换 len()计算数据的长度
"""
print("hello world")  # 字符串
print(2333)  # 整数
print(2.333)  # 浮点数
print(True)  # 布尔值
print(())  # 元组
print([])  # 列表
print({})  # 字典

哈哈

print("哈哈",2333,2.333)
print("哈哈"+"嘻嘻")  # 字符串的拼接 同样的类型
print("哈哈"*50)
print(((1+2)*100-9.9)/2)
print(2>3)

name = "张三"  # 把 张三 这个值赋值给了名字叫name的这个变量
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

# a = int("2333")  # 字符串转整数
# print(type(a))

# 两种方法
# a = input("请输入：")
# b = input("请输入：")
# print("input获取的内容:",int(a)+int(b))

# a = float(input("请输入："))
# b = float(input("请输入："))
# print("input获取的内容:",a+b)

# a = "嘻嘻"
# print(len(a))
"""
练习：通过代码获取两段内容，并且计算他们长度的和。123
"""
# a = input("请输入内容：")
# b = input("请输入内容：")
# print(len(a+b))

# 元组，下标 从左从0开始编号  从右从-1开始编号 -1 -2
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a[-2])

# #切片
# print(a[:4])  # 左闭右开
# print(a[4:9])
# print(a[9:])

# print(a.index("哈哈"))  # 查找某个值的下标 一维元组才能使用
# print(a.count("哈哈"))  # 统计某个值的数量 一维元组才能使用

#二维元组
# b = (a,"哈哈","嘻嘻")
# print(b[0][3])  # b[0]等于一维元组a

# 列表
# 区别 元组一旦写好过后不可以修改 列表写好后可以修改
# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# a.append("append")  # 往列表中追加数据
# print(a)

# a.insert(4,"insert")  # 往列表中指定的位置插入数据 输入下标
# print(a)

# b = a.pop(0)  # 剪切 1
# c = a.pop(0)  # 剪切 2
# print(b+c)
# print(a)

# a.clear()  # 清空数组
# print(a)
# xx = ["你好","不好"]
# a.extend(xx)  #合并列表 类似append 追加列表中的值
# print(a+xx)
# print(a)

# b = a.remove("哈哈")
# print(b)

# a.remove("哈哈")  #删除某个值 不是下标
# print(a)

# 注意事项
# false=0 true=1
# xx = [0,False,1,True]
# a = xx.count(0)
# print(a)

# 下标不要超出范围 = 越界
# xx = [0,1,2,3]
# print(xx[9])

"""
python语法 规律
所有的方法都是用小括号结尾，比如：print(),input(),len()
元组、列表、字典的取值，都是用中括号，比如：a[0]
元组、列表、字典的定义，分别是(),[],{}
"""
"""
字典的特点
1、字典中的值没有顺序
2、字典的结构必须是 键值对 的结构：key:value
"""
a = {"name":"张三",0:"哈哈","age":25} # 可以理解为自定义了下标
# 取值
print(a["name"])
# 新增
a["height"] = "185cm"
print(a)
# 修改
a["name"] = "李四"
print(a)

b = a.get("name")
print(b)

# 剪切
# b = a.pop("name")
# print(b)
# print(a)

# 更新
a.update(name = 1111)
print(a)

print("-----------------")
print(a.get("name111"))
# 打印不存在的key时 会报错 上面的get不会
# print(a["name111"])