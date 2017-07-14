#!/usr/bin/python
# Author: LiTianle
# -*- coding:utf-8 -*-
# 一、购物车
# 功能要求：
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
################################################################################################################################################
tag_1=True
tag_2=True
tag_3=True
tag_4=True
tag_5=True
tag_6=True
buy_list=[]
total=0
#声明4层循环状态为true，定义空购物车列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
print('欢迎光临python超市!可供购买的商品如下：')
for n,v in enumerate(goods,1):#打印商品信息
    print(n,'ProductName:{name}\tPrice:{price}'.format(name=v['name'],price=v['price']))
while tag_1:#开始一级循环
    money=input('输入会员卡中余额：').strip()#提示输入余额并去空
    if len(money) == 0 or not money.isdigit():#判断输入长度是否为0或者是否为数字
        print('输入有误，请重新输入(数字)！')
        continue#是的话，继续循环
    else:
        money=int(money)#转换money类型为int
        while tag_2:#开始二级循环
            choice_id=input('请选择要购买的商品序号：').strip()#提示用户选择商品序号
            if not choice_id.isdigit() or len(choice_id)==0 or int(choice_id)>len(goods):#判断是否数字、长度是否为0、输入序号是否在可选范围内
                print('输入有误，请重新输入！')
                continue#输入有误，继续循环提示输入
            else:#输入正确
                buy_list.append(goods[int(choice_id) - 1]['name'])  # 将商品加入购物车
                total+=goods[int(choice_id) - 1]['price']#合计累加
                s=set(buy_list)
                for i in s:
                    print('Name:%s 数量：%s' % (i, buy_list.count(i)))
                print('购买成功,合计：%s'% total)
                tag_3=True
                while tag_3:#开始三级循环
                    buy_YN=input('是否继续购买？Y or N：').strip()
                    if len(buy_YN)==0 or buy_YN not in ('Y','N'):#判断长度是否为0、是否为Y或N
                        print('输入有误，请重新输入！(Y or N)')
                        continue
                    elif buy_YN == 'Y':
                        tag_3=False#继续购买，结束本次——循环3，继续购买——循环2
                    elif buy_YN == 'N':#不继续购买
                        if money >= total:#判断余额是否>=合计，是的话打印结束语以及购物车信息，终止所有循环
                            print('谢谢光临，再见')
                            s = set(buy_list)
                            for i in s:
                                print('Name:%s 数量：%s' % (i, buy_list.count(i)))
                            print('找零：%s' % (money-total))
                            tag_3=False
                            tag_2=False
                            tag_1=False
                        else:#余额不足
                            while tag_4:
                                chongzhi_YN = input('余额不足，是否充值（Y or N）：').strip()#是否充值
                                if len(chongzhi_YN) == 0 or chongzhi_YN not in ('Y', 'N'):
                                    print('输入有误，请重新输入！(Y or N)')
                                    continue
                                elif chongzhi_YN == 'N':#余额不足还不充值走循环6
                                    while tag_6:
                                        s = set(buy_list)
                                        for i in s:
                                            print('Name:%s 数量：%s' % (i, buy_list.count(i)))
                                        print('找零：%s' % (money - total))#打印目前购物车信息
                                        del_choice=input('请输入要放弃的商品名称：（q退出）').strip()#提示选择删除的商品
                                        if del_choice in buy_list:#删除并且合计-删除的商品价格
                                            buy_list.remove(del_choice)
                                            for i in goods:
                                                if i['name'] == del_choice:
                                                    total -= i['price']
                                            if money<total:#删除后还买不了继续删除
                                                print('余额还是不足，继续吧')
                                                continue
                                            else:#当删除到可以购买时结束，终止所有循环
                                                print('谢谢光临，再见')
                                                s = set(buy_list)
                                                for i in s:
                                                    print('Name:%s 数量：%s' % (i, buy_list.count(i)))
                                                print('找零：%s' % (money - total))
                                                tag_6 = False
                                                tag_4 = False
                                                tag_3 = False
                                                tag_2 = False
                                                tag_1 = False
                                        elif len(del_choice) == 0:
                                            print('不能为空')
                                            continue
                                        elif del_choice == 'q':#q放弃本次购物，终止所有循环
                                            print('很遗憾，你放弃了本次购物')
                                            tag_6 = False
                                            tag_4 = False
                                            tag_3 = False
                                            tag_2 = False
                                            tag_1 = False
                                else:
                                    while tag_5:
                                        chongzhi_money=input('请输入充值金额：')
                                        if len(chongzhi_money) == 0 or not chongzhi_money.isdigit():  # 判断输入长度是否为0、是否是数字
                                            print('错误，请输入数字！')
                                            continue
                                        else:#输入正确，走充值
                                            money = money + int(chongzhi_money)  # 将充值金额加到余额
                                            print('充值成功！余额为:',money)
                                            if money < total:
                                                print('充的不够，继续充,目前的余额为%s'%money)
                                                continue
                                            else:
                                                print('谢谢光临，再见')
                                                s = set(buy_list)
                                                for i in s:
                                                    print('Name:%s 数量：%s' % (i, buy_list.count(i)))
                                                print('找零：%s' % (money - total))
                                                tag_5 = False#跳出当前循环，继续走购物
                                                tag_4 = False
                                                tag_3 = False
                                                tag_2 = False
                                                tag_1 = False
