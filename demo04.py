"""
class 声明类的名字
然后类的名字的首字母必须大写
面向对象编程
默认属性方法__init__ 使用__init__来接受参数
类里面所有的方法，都必须要传一个参数，叫self

继承 重写/多态
"""

class Girlfriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weigh,hair,age):
        """
        女朋友 属性
        """
        self.sex = sex
        self.high = high
        self.weigh = weigh
        self.hair = hair
        self.age = age
    
    def caiyi(self,num):
        """
        才艺表演
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weigh+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的才艺表演之:")
        if num == 1:
            print("胸口碎大石！")
        elif num == 2:
            peint("唱、跳、rap、篮球")
        else:
            print("单手开瓶盖")
    
    def chuyi(self):
        """
        厨艺持家
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weigh+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的厨艺表演之:")
        print("精通八大菜系！啥都会！")

    def work(self):
        """
        工作挣钱
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weigh+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的工作之:")
        print("开挖掘机！")

# # 类的实例化
# zhangsan = Girlfriend("男","188cm","70kg","锡纸烫","24")
# zhangsan.caiyi(1)
# zhangsan.chuyi()
# zhangsan.work()
# print(zhangsan.sex)

# class Car():
#     def __init__(self,pingpai,yanse,neishi,jilun):
#         self.pingpai = pingpai
#         self.yanse = yanse
#         self.neishi= neishi
#         self.jilun = jilun

#     def bianxing(self):
#         print("车子变身金刚喜羊羊！")

#     def fly(self):
#         print("车子开始起飞！")

# zhangsan = Car("奥拓","五颜六色","豪华","独轮")
# zhangsan.bianxing()
# print(zhangsan.pingpai)

class Nvpengyou(Girlfriend):
    def work(self):
        print("修电脑")
    #pass  #占位 没有作用 防止代码没写完 报错

zhangsan = Nvpengyou("女","165cm","50kg","大波浪","20")
zhangsan.caiyi(1)
zhangsan.work()

# object 祖宗类
# Girlfriend 父类     Nvpengyou 子类 可以修改覆盖掉父类的方法叫做重写/多态