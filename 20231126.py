#字典：表示映射结构；dict={key1:value1,key2:value2,....}
#创建字典时有两种方法：name={}或者name=dict()
#在像字典中添加键值对时，语法格式为dictname[key]=value;key表示映射的健，key表示value的值

# #price={}
# price=dict()
# price["苹果"]=5
# price["桃子"]=6
# price["香蕉"]=3
# price["梨子"]=4
# price["火龙果"]=7
# print(price)
#
# if '苹果' in price:
#     print('苹果的价格%d'%(price['苹果']))
# else:
#     print('该水果不卖')
# if '荔枝' in price:
#     print('荔枝的价格%d'%(price['荔枝']))
# else:
#     print('该水果不卖')
# # print(price['荔枝'])

# #统计水果总金额的python代码
# #定义水果的价格字典
# price=dict()
# price["苹果"]=5
# price["桃子"]=6
# price["香蕉"]=3
# price["梨子"]=4
# price["火龙果"]=7
# print(price)
# #通过循环，配合相应的信息，将字典中的水果与价格打印出来
# for fruit in price:
#     print("%s%d元/斤"%(fruit,price[fruit]))
#     print("")
#
# #输入购买水果的种类数量，存储到变量n中
# n=int(input('请输入购买水果的种类数量'))
# #设置sum_price存储总金额
# sum_price=0
# #输入购买的水果名称与数量，存储至fruit与num
# for i in range(0,n):
#     fruit=input('输入购买的水果%d的名称：'%(i+1))
#     num=int(input('输入购买的水果%d的数量（斤）：'%(i+1)))
#
# #如果输入的说过在price字典中，将水果单价price[fruit]购买的数量num累加到sum_price
# if fruit in price :
#     sum_price+=price[fruit]*num
# print("总价格为%d"%(sum_price))


A={'a':85,'b':96,'c':88}
B={'a':72,'b':80,'c':91}
C={'a':83,'b':69,'c':75}

# sum_A=A['a']+A['b']+A['c']
# sum_B=B['a']+B['b']+B['c']
# sum_C=C['a']+C['b']+C['c']
#
# print(sum_A,sum_B,sum_C)
# MAX=max(sum_A,sum_B,sum_C)
# print(MAX)

# python的关系运算
# # 布尔运算：True=1,False=0
# v1=True
# v2=False
# v3=True
# print(v1)
# print(v2)
# print(int(v1))
# print(int(v2))
# print(v1+v3)

#关系运算符：>,<,>=,<=,==,!=,运算结果是布尔值

#
a=int(input("请输入我们球队的实力"))
b=int(input("输入我们对手1对队的实力："))
c=int(input("请输入我们对手2队的实力："))
d=int(input("请输入我们对手3队的实力："))
avsb=(a>b)*3+(a==b)
avsc=(a>c)*3+(a==c)
avsd=(a>d)*3+(a==d)
score=avsc+avsd+avsb
print(score)






