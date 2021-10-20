# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_culture = Blueprint('culture', __name__, url_prefix='/culture/',
                     static_url_path='',
                     static_folder='.',
                     template_folder='.',
                     )

# 主页面
@_culture.route('/main')
def cultureindex():
    return render_template('main.html')


@_culture.route('/2019')
def culture2019():
    return render_template('2019.html')


@_culture.route('/2020')
def culture2020():
    return render_template('2020.html')
