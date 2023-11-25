# print()函数表达
# print('*****')
# print('*****')
# print('*****')
# print('*****')
# print('*****')

# for循环
# for i in range(0,10):   # i为循环变量，循环范围是0-9；range(a,b)会生成a,.....,b-1
#     print("i=%d"%(i))

#练习for循环
# rabbit=3 #初始兔子的数量
# print("请输入N的值：")  #第N年的信息
# N=int(input())    #屏幕输入数值
# for i in range(0,N):  #循环语句
#     rabbit=rabbit*2
# print("%d年后，兔子的数量为%d."%(N,rabbit))  #打印兔子的数量

# Num=1
# print("请输入N的值：")
# N=int(input())
# for i in range(1,N):
#     Num = Num + 1
#     sum= (Num+1)*Num/2
# print("%d，总和为%d."%(N,sum))

# print("请输入N的值：")
# N=int(input())
# for i in range(1,N):
#     sum= (N+1)*N/2
# print("%d，总和为%d."%(N,sum))

#集合，与字典类似，集合之间的内容用逗号隔开，集合内部存储的为不可变的基础数据类型（整型、浮点型、字符串型、元组）
#可变的数据类型为：列表，集合，字典
#集合创建可以set()或者{初始集合元素}，创建空集只能用set(),不能用{}
#集合是无序的，不可以用索引访问，可以用遍历来访问
# a=set()
# b={1,2,'ab'}
# print(a)
# print(b)

# 集合间的运算：交集使用&、intersion；并集使用|、union;差集使用-、difference
# a={1,2,3,4}
# b={3,4,5,6}
# print(a&b)
# print(a.intersection(b))
# print(a|b)
# print(a.union(b))
# print(a-b)
# print(b.difference(a))

num1=int(input("输入班级1的学生数量："))
class1=set()
for i in range(0,num1):
    name=input("输入学生%d姓名："%(i+1))
    class1.add(name)

num2=int(input("输入班级2的学生数量："))
class2=set()
for i in range(0,num2):
    name=input("输入学生%d姓名："%(i+1))
    class2.add(name)
same=class2 - class1
print("重名的学生：")
for name in same:
    print(name)

