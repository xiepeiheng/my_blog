# -*- codeing = utf-8 -*-
import sqlite3
from setting import *
from function.sqlite_function import *
from function.sqlite_function import *


def diary(table_name, jsk):
    con, cur = db_open()
    cmy = sqliteObject_to_list_a(cur, f'''
        select e from {table_name}
    ''')

    # cmy = ['\\2020\\2020_08\\2020-08-01_本日记录.html',
    #        '\\2020\\2020_08\\2020-08-02_本日记录.html',
    #        '\\2021\\2021_08\\2021-08-01_本日记录.html',
    #        '\\2021\\2021_08\\2021-08-02_本日记录.html',
    #        ]
    # 2021\2021_08\2021-08-02_本日记录.html,2021,08,2021-08-02_本日记录

    html_name = jsk
    f = open(html_name, 'w')
    temp_year = ''
    temp_month = ''
    html = ''
    for i in cmy:

        address = i[1:].replace('\\', '/')
        zfh = i.split('\\')
        year = zfh[1]
        month = zfh[2].split('_')[1]
        name = zfh[3][:-5]
        if temp_year != year:
            temp_year = year
            html = html + f'''
            <div><button year="{year}" month="0" class="year">{year}年</button></div>
            '''
            temp_month = ''
        if temp_month != month and temp_year == year:
            temp_month = month
            html = html + f'''
            <div><button year1="{year}" month="{month}" class="month">{month}月</button></div>
            '''

        html = html + f'''
        <div><button year1="{year}" month1="{month}" class="day" address="{address}">{name}</button></div>
        '''
    # 写入文件
    f.write(html)
    # 关闭文件
    f.close()

    print('diary目录完成')


def computer(table_name, jsk):
    con, cur = db_open()
    cmy = sqliteObject_to_list_a(cur, f'''
        select e from {table_name}
    ''')
    # 数据格式：\JavaScript\2021 - 01 - 01_Ajax.html
    html_name = jsk
    f = open(html_name, 'w')
    html = ''
    folder = ''

    for i in cmy:
        folder_name = i.split('\\')[1]
        name = i.split('\\')[2].split('_')[1].split('.')[0]
        # name = os.path.split()
        address = i[1:].replace('\\', '/')

        if folder_name != folder:
            folder = folder_name
            html = html + f'''
            <div><button folder="{folder_name}" class="folder">{folder_name}</button></div>
            '''
        html = html + f'''
        <div><button class="name" folder1="{folder_name}" address="{address}">{name}</button></div>
        '''
    # 写入文件
    f.write(html)
    # 关闭文件
    f.close()

    db_close(con, cur)
    print('computer目录完成')


def important(table_name, jsk):
    con, cur = db_open()
    cmy = sqliteObject_to_list_a(cur, f'''
        select e from {table_name}
    ''')
    # 数据格式：\重要文件夹1\2021 - 01 - 01_Ajax.html
    html_name = jsk
    f = open(html_name, 'w')
    html = ''
    folder = ''

    for i in cmy:
        folder_name = i.split('\\')[1]
        name = i.split('\\')[2].split('_')[1].split('.')[0]
        # name = os.path.split()
        address = i[1:].replace('\\', '/')

        if folder_name != folder:
            folder = folder_name
            html = html + f'''
            <div><button folder="{folder_name}" class="folder">{folder_name}</button></div>
            '''
        html = html + f'''
        <div><button class="name" folder1="{folder_name}" address="{address}">{name}</button></div>
        '''
    # 写入文件
    f.write(html)
    # 关闭文件
    f.close()

    db_close(con, cur)

    print('important目录完成')



