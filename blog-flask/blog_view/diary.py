# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_diary = Blueprint('diary', __name__, url_prefix='/diary',
                   static_url_path='',
                   static_folder='../total/日志系统',
                   template_folder='../total/日志系统',
                   )


# 日志页面导览
@_diary.route('/home')
def diary1():
    return render_template('diary_index.html')


# 返回选择的日期
@_diary.route('/<a>')
def diary2(a):
    return render_template(a)
