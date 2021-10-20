# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect, request

_index = Blueprint('index', __name__, url_prefix='/index',
                        static_url_path='',
                        static_folder='.',
                        template_folder='.',
                        )

# 日志页面导览
@_index.route('/')
def index1():
    return render_template('index.html')


@_index.route('/language', methods=['POST'])
def index2():
    if request.form['a'] == '1':
        return render_template('index-cn.html')
    if request.form['a'] == '2':
        return render_template('index-jp.html')





