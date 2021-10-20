# -*- codeing = utf-8 -*-
from setting import *
import os
import sqlite3
from function.sqlite_function import *
import pypandoc
import shutil
from blog_view.init_db.md_to_html import *
from blog_view.init_db.make_catalogue import *
from setting import *

f1 = [diary_old_path, diary_new_path, diary_tablename]
f2 = [computer_old_path, computer_new_path, computer_tablename]
f3 = [important_old_path, important_new_path, important_tablename]
# f4废弃
# f4 = [language_old_path, language_new_path, language_tablename]

# 请输入你想要重新生成html目录的文件夹,想换哪个就放哪个
flod = [f1,f2,f3]


def main(flod):
    for i in flod:
        cmy = address1(i[0], i[1])
        save(cmy, i[2])
        make(cmy, i[1])
        convert1(cmy)
        if i[2] == 'diary':
            print('开始生成diary目录文件')
            html_address = diary_new_path + '\\' + diary_tablename + '.html'
            diary(i[2], html_address)
        if i[2] == 'computer':
            print('开始生成computer目录文件')
            html_address = computer_new_path + '\\' + computer_tablename + '.html'
            computer(i[2], html_address)
            print(html_address)
        if i[2] == 'important':
            print('开始生成important目录文件')
            html_address = important_new_path + '\\' + important_tablename + '.html'
            important(i[2], html_address)


main(flod)


