# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_important = Blueprint('important', __name__, url_prefix='/important',
                       static_url_path='',
                       static_folder='../total/重要文件',
                       template_folder='../total/重要文件',
                       )


# 日志页面导览
@_important.route('/home')
def important1():
    return render_template('important_index.html')


# 返回选择的日期
@_important.route('/<a>')
def important2(a):
    return render_template(a)
