#!/usr/bin/python
# Author:LiTianle
# -*- coding:utf-8 -*-
with open('user_info_db.txt','r',encoding='utf-8') as f:
    user_info_str=f.read()
user_info_str=user_info_str.split('\n')
user_info={}

for i in user_info_str:
    ii=(i.split('|'))
    dic={
        ii[0]:{'password':ii[1],'time':ii[2]}
    }
    user_info.update(dic)
print(user_info)

# with open('black_list.txt','r',encoding='utf-8') as f:
#     black_list_str=f.read()
tag=True
while tag:
    user_name=input('plz input your name: ')
    if len(user_name)==0:
        print('input can not empty')
    elif user_name not in user_info:
        print('user not exist')
        continue
    elif int(user_info[user_name]['time']) >= 3:
        print('user locked!')
        continue
    else:
        user_password = input('plz input your password: ')
        if len(user_password) == 0:
            print('input can not empty')
        elif user_password==user_info[user_name]['password']:
            print('login sucessful!')
            user_info[user_name]['time']='0'
            i_list = []
            for i in user_info:
                i_tmp_1 = i, user_info[i]['password'], str(user_info[i]['time'])
                # i_tmp_1 = i, user_info[i]['password'],user_info[i]['time']
                # print(i_tmp_1, type(i_tmp_1))
                i_tmp_2 = '|'.join(i_tmp_1)
                i_list.append(i_tmp_2)
            # print(i_list)
            end_str = '\n'.join(i_list)
            # print(end_str)
            with open('user_info_db1.txt', 'w', encoding='utf-8') as f:
                f.write(end_str)
            tag=False

        else:
            user_info[user_name]['time']=int(user_info[user_name]['time'])+1
            # user_info[user_name]['time'] = str(user_info[user_name]['time'])
            print('password error,plz input agin!', user_info[user_name]['time'])
            if int(user_info[user_name]['time']) >=3:
                print('失败次数超3次，账户锁定，请联系管理员！')
                i_list = []
                for i in user_info:
                    i_tmp_1 = i, user_info[i]['password'], str(user_info[i]['time'])
                    # i_tmp_1 = i, user_info[i]['password'],user_info[i]['time']
                    # print(i_tmp_1, type(i_tmp_1))
                    i_tmp_2 = '|'.join(i_tmp_1)
                    i_list.append(i_tmp_2)
                # print(i_list)
                end_str = '\n'.join(i_list)
                # print(end_str)
                with open('user_info_db.txt', 'w', encoding='utf-8') as f:
                    f.write(end_str)
                tag=False
