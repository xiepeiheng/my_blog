# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_cv = Blueprint('cv', __name__, url_prefix='/cv',
                        static_url_path='',
                        static_folder='.',
                        template_folder='.',
                        )


@_cv.route('/')
def cv1():
    return render_template('cv.html')