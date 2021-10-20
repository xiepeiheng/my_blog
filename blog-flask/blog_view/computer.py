# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_computer = Blueprint('computer', __name__, url_prefix='/computer',
                      static_url_path='',
                      static_folder='../total/专业笔记',
                      template_folder='../total/专业笔记',
                      )


# 日志页面导览
@_computer.route('/home')
def computer1():
    return render_template('computer_index.html')


# 返回选择的日期
@_computer.route('/<a>')
def computer2(a):
    return render_template(a)
