# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_graduation = Blueprint('graduation', __name__, url_prefix='/graduation',
                        static_url_path='',
                        static_folder='.',
                        template_folder='.',
                        )


@_graduation.route('/')
def graduation():
    return render_template('graduation.html')