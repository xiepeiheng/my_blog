# -*- codeing = utf-8 -*-
from flask import Blueprint, render_template, redirect

_gallery = Blueprint('gallery', __name__, url_prefix='/gallery',
                        static_url_path='',
                        static_folder='.',
                        template_folder='.',
                        )


@_gallery.route('/')
def gallery1():
    return render_template('gallery.html')