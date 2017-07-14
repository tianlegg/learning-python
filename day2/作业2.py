#!/usr/bin/python
# Author:LiTianle
# -*- coding:utf-8 -*-
dic={
    'A':{
        'AA':['AA1','AA2','AA3'],
         'AB':['AB1','AB2','AB3'],
         'AC':['AC1','AC2','AC3']},
    'B':{
        'BA':['BA1','BA2','BA3'],
        'BB':['BB1','BB2','BB3'],
        'BC':['BC1','BC2','BC3']},
    'C':{
        'CA':['CA1','CA2','CA3'],
        'CB':['CB1','CB2','CB3'],
        'CC':['CC1','CC2','CC3']}
}
tag1=True#一级循环
tag2=True#二级循环
while tag1:#一级循环开始
    for i in dic.keys():
        print(i)  # 打印一级目录
    k1=input('plz input first menus: ').strip()#接收用户输入的一级目录选项
    if len(k1) == 0 or k1 not in dic.keys():#判断输入长度以及是否在一级目录中
        print('plz check your input')
        continue
    else:
        for x in dic[k1].keys():#打印二级目录
            print(x)
    while tag2:#开始二级循环
        k2=input('plz input second menus: ').strip()#接收用户输入的二级目录选项
        if len(k2) == 0 or k2 not in dic[k1].keys():#判断输入长度以及是否在二级目录中
            print('plz check your input')
            continue
        for y in dic[k1].keys():#打印三级目录
            if y==k2:
                for s in dic[k1][k2]:
                    print(s)
                # print(dic[k1][k2])
        tag2=False
    YN=input('Return to previous menu:(Y or N) ').strip()#是否继续查询
    if YN == 'Y':#继续的话重置二级循环状态，并重新开始一级循环
        tmp='#'
        print(tmp.center(20,'#'))
        tag2=True
    else:#不继续的话，退出
        print('Bye~Bye!')
        tag1=False