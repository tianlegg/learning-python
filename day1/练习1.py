#!/usr/bin/python
# -*- coding:utf-8 -*-
#1、简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型
#编译型语言是需要编译器编译后再运行的，解释型语言是直接逐行读取运行的；解释型语言：python、php、; 编译型语言：java、c、c++
#2、执行 Python 脚本的两种方式是什么
#一种是文件头标记python解释器，直接运行文件；第二种是python解释器路径+文件名
#3、 Pyhton 单行注释和多行注释分别用什么?
#单行注释“#”，多行注释''' '''
#4、布尔值分别有什么？
#True: 非0、None、空元素的都为True
#False ：0、None、""、()、{}、[]
#5、声明变量注意事项有那些?
#声明变量时，只能是下划线、字母、数字等元素的组合，而且不能以数字开头且不能和内置变量名冲突
#6、如何查看变量在内存中的地址?
#通过id查看变量的内存地址
#7、写代码
# 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
# user_name=input('plz input your name: ')
# user_password=input('plz input your password: ')
# if user_name == 'seven' and user_password=='123':
#     print('登录成功')
# else:
#     print('登录失败，帐号密码错误')
# 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
#-------------
# count=0
# while True:
#     user_name = input('plz input your name: ')
#     user_password = input('plz input your password: ')
#     if user_name == 'seven' and user_password == '123':
#         print('登录成功')
#     else:
#         print('登录失败，帐号密码错误')
#         count+=1
#         if count < 3:
#             continue
#         else:
#             print('失败次数超过三次，请重试')
#             break
#---------------
# tag=True
# count=0
# while tag:
#     user_name = input('plz input your name: ')
#     user_password = input('plz input your password: ')
#     if user_name == 'seven' and user_password == '123':
#         print('登录成功')
#         break
#     else:
#         count+=1
#         print('登录失败，帐号密码错误')
#         if count==3:
#             tag=False
#------------
# 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# dic={'name':['seven','alex'],'password':'123'}
# count=0
# while True:
#     user_name = input('plz input your name: ')
#     user_password = input('plz input your password: ')
#     if user_name in dic['name'] and user_password==dic['password']:
#         print('登录成功')
#         break
#     else:
#         count+=1
#         if count ==3:
#             print('失败次数过多，请重新执行程序')
#             break
#         else:
#             print('登录失败，请重试')
#8、写代码
# a. 使用while循环实现输出2-3+4-5+6...+100 的和
# count=2
# sum=0
# while count <=100:
#     if count%2==0:
#         sum += count
#         count+=1
#     else:
#         sum -= count
#         count+=1
# print(sum)


# b. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
# count=1
# while True:
#     if count <=12:
#         if count in [6,10]:
#             count+=1
#             continue
#         else:
#             print(count)
#             count+=1

# d. 使用 while 循环实现输出 1-100 内的所有奇数
# count=1
# while True:
#     if count > 100:
#         break
#     else:
#         if (count%2):
#             print(count)
#             count+=1
#         else:
#             count+=1



# e. 使用 while 循环实现输出 1-100 内的所有偶数
# count=1
# while count <100:
#     if (count%2):
#         count+=1
#         continue
#     else:
#         print(count)
#         count+=1

#9、现有如下两个变量,请简述 n1 和 n2 是什么关系?
# n1 = 123456
# n2 = n1
# n1和n2都指向了123456的内存地址，两个变量之间独立的，没有直接关系
# id/type/值都是相同的
# print(id(n1))
# print(type(n1))
# print(n1)
#
# print(id(n2))
# print(type(n2))
# print(n2)

#11使用while循环输出1 2 3 4 5 6     8 9 10
# i=1
# while i<=10:
#     if i==7:
#         i+=1
#         continue
#     else:
#         print(i)
#         i+=1

#12、 求1-100的所有数的和
# i=1
# sum=0
# while i <=100:
#     sum+=i
#     i+=1
# print(sum)
#13、 输出 1-100 内的所有奇数
# i=1
# while i <=100:
#     if i%2:
#         print(i)
#         i+=1
#     else:
#         i+=1
#14、 输出 1-100 内的所有偶数
# i=1
# while i <=100:
#     if i%2:
#         i+=1
#     else:
#         print(i)
#         i+=1
#15、求1-2+3-4+5 ... 99的所有数的和
# i=1
# sum=0
# while i <100:
#     if i%2:
#         sum+=i
#         i+=1
#     else:
#         sum-=i
#         i+=1
# print(sum)
#16、用户登陆（三次机会重试）
# count=0
# while True:
#     user_name=input('plz input your name: ')
#     user_password=input('plz input your password: ')
#     if user_name =='Tianle' and user_password=='123':
#         print('登录成功')
#         break
#     else:
#         print('用户名密码错误,请重试！')
#         count+=1
#         if count >=3:
#             break

