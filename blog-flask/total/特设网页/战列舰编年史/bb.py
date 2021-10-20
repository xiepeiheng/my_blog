# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for

_bb = Blueprint('bb', __name__, url_prefix='/bb',
                static_url_path='',
                static_folder='.',
                template_folder='.',
                )


@_bb.route('/')
def bb():
    return render_template('bb.html')
