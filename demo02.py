# 判断 由 缩进 代表 代码块
# a = 1
# b = 2
# if a == 1:
#     print("哈哈哈")

# if a > b:
#     print("a比b大")
# else：
#     print("b更大")

# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("您应该退休了")
# elif age > 30:
#     print("家庭的责任很重吧")
# elif age > 20:
#     print("一定要好好规划你的未来!")
# else:
#     print("读书的时候 要认真！")

# if age > 20 and age <= 30:  # 多条件同时满足
#     print("22222222")  

# 判断条件 ==,!=,>,<,in,is,not in,not is 

# a = "你好"
# if a in "你好，今天你吃了吗？":
#     print("OK")
# else:
#     print("不OK")

# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()

# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()

# if a > 5:
#     print("大")
# else:
#     print("小")

# a = "aaa"
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# 循环 while for
# a = 1
# while a < 10:
#     print("哈哈哈",a)
#     a = a + 2

"""
练习：现在有10个学生的成绩，需要录入到系统中，
这10个人分别是：张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠
并且名字和成绩需要对应上 而已大于60和小于60的要分开存放
"""
"""
# while 方法
high = {}  # 定义了一个空字典 用来存储大于60的成绩
low = {}  # 定义了一个空字典 用来存储小于60的成绩
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠"]  # 定义了一个列表 用来存储姓名
a = 0  # 定义了一个变量 用来控制数组的下标变化
while a < len(studentlist):  # 因为所有的录入都是要用input，所以写了循环，len判断了数组的长度
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))  # 录入信息 为了方便判断 所以转换成整数
    if chengji >= 60:  # 判断分数
        high[studentlist[a]] = chengji  # 存到字典中
    else:
        low[studentlist[a]] = chengji
    a = a + 1  # 控制下标变化 每一次循环 都+1
print("大于60的：",high)
print("小于60的：",low)
"""
# for方法
# high = {}  # 定义了一个空字典 用来存储大于60的成绩
# low = {}  # 定义了一个空字典 用来存储小于60的成绩
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠"]  # 定义了一个列表 用来存储姓名
# for i in studentlist:
#     chengji = int(input("请输入"+i+"的成绩："))  # 录入信息 为了方便判断 所以转换成整数
#     if chengji >= 60:  # 判断分数
#         high[i] = chengji  # 存到字典中
#     else:
#         low[i] = chengji
# print("大于60的：",high)
# print("小于60的：",low)

# 遍历
# a = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠"]
# for i in a:
#     print(i)
# 数列生成器 range() 
# b = list(range(0,100,2))  # 自动生成了一个数列,步进/步长
# print(b)

# for i in range(100):
#     print(i)

"""
练习：打印九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end=" ")
    print()