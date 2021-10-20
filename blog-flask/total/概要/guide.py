# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_guide = Blueprint('guide', __name__, url_prefix='/guide',
                        static_url_path='',
                        static_folder='.',
                        template_folder='.',
                        )


@_guide.route('/')
def guide1():
    return render_template('guide.html')