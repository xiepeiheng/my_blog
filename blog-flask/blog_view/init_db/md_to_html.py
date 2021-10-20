# -*- codeing = utf-8 -*-
from setting import *
import os
import sqlite3
from function.sqlite_function import *
import pypandoc
import shutil


# md转html核心模块 只需要给出两个文件夹的地址就能实现转换


def address1(old_path, new_path):
    hxy = os.walk(old_path, topdown=False)

    # a 旧位置绝对地址
    # C:\\Users\\谢佩恒\\Desktop\\my-blog\\blog\\md_database\\diary\\2020\\2020_07\\2020-07-01_本日记录.md
    # b 旧位置绝对地址（不带文件名称）
    # C:\\Users\\谢佩恒\\Desktop\\my - blog\\blog\\md_database\\diary\\2020\\2020_07
    # c 新位置的绝对地址（后缀是html）
    # C:\\Users\\谢佩恒\\Desktop\\my-blog\\blog\\total\\日志系统\\2020\\2020_07\\2020-07-01_本日记录.html
    # d 新位置绝对地址（不带文件名称）
    # C:\\Users\\谢佩恒\\Desktop\\my-blog\\blog\\total\\日志系统\\2020\\2020_07
    # e 旧位置相对于新位置的地址（比如2021/27/21/2021-27-21.md这样的地址）
    # \\2020\\2020_07\\2020-07-01_本日记录.html
    # f 旧位置相对于新位置的地址（不带文件名称）
    # \\2020\\2020_07
    # name 文件名称
    # name1 不要后缀和前面时间的名称（用作网页上对应的标题）

    # 原始数据
    cmy = []
    # 处理后的数据
    zfh = []
    for a, b, c in hxy:
        if b == []:
            for i in c:
                cmy.append(a + '\\' + i)
    for i in cmy:
        a = i
        b = os.path.split(i)[0]
        jsk = i.split('\\')
        temp1 = old_path.split('\\')[-1]
        length1 = len(jsk)
        for temp in range(length1):
            if jsk[temp] == temp1:
                c = new_path
                e = ''
                for temp2 in jsk[-(length1 - temp - 1):]:
                    c = c + '\\' + temp2
                    e = e + '\\' + temp2
                break
        m1 = os.path.split(e)[0]
        m2 = os.path.split(e)[1]
        m3 = os.path.splitext(m2)[0] + '.html'
        e = m1 + '\\' + m3
        k1 = os.path.split(c)[0]
        k2 = os.path.split(c)[1]
        k3 = os.path.splitext(k2)[0] + '.html'
        c = k1 + '\\' + k3
        d = os.path.split(c)[0]
        f = os.path.split(e)[0]
        name = os.path.split(c)[1]
        # 单纯的名字，这点可以高度定制
        name1 = os.path.splitext(name)[0].split('_')[1]
        zfh.append([a, b, c, d, e, f, name, name1])
        # print([a,b,c,d,e,f,name,name1])

    print('地址解析完成')
    return zfh


def save(cmy, name):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # 将diary表中的内容删除，没有这个表就创建一个
    table = sqliteObject_to_list_a(cur, f'''
        select name from sqlite_master
    ''')
    if name in table:
        cur.execute(f'delete from "{name}"')
    else:
        sql = f'''
            create table '{name}'
            (
                a text,
                b text,
                c text,
                d text,
                e text,
                f text,
                name text,
                name1 text
            );
        '''
        cur.execute(sql)

    for i in cmy:
        sql = f'''
            insert into '{name}'(
                a,
                b,
                c,
                d,
                e,
                f,
                name,
                name1
            )
            values(
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            '''
        cur.execute(sql, (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
    con.commit()
    cur.close()
    con.close()

    print('存储完成')


def make(cmy, new_path):
    # 先清空文件夹内的现有文件，除了模板html
    path = new_path
    cmy1 = os.listdir(path)
    for i in cmy1:
        path1 = path + '\\' + i
        if os.path.isdir(path1):
            shutil.rmtree(path1)

    for i in cmy:
        zfh = i[5].split('\\')[1:]
        newpath = new_path
        for k in zfh:
            newpath = newpath + '\\' + k
            if os.path.exists(newpath):
                os.chdir(newpath)
            else:
                os.mkdir(newpath)
                os.chdir(newpath)

    print('文件目录创建完成')


def convert1(cmy):
    for i in cmy:
        extra_args = (
            '--css', r'C:\Users\谢佩恒\Desktop\my-blog\测试\my.css',
            '--self-contained',
        )
        hxy1 = r'{a}'.format(a=i[0])
        hxy2 = r'{b}'.format(b=i[2])
        pypandoc.convert(hxy1, 'html', format='md', extra_args=extra_args, encoding='utf-8', outputfile=hxy2)
    print('html创建完成')
