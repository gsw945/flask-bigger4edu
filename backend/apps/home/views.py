# -*- coding: utf-8 -*-
'''站点首页视图'''
from flask import render_template

from . import home_app, app_name


@home_app.route(r'/')
def view_index():
    return render_template(app_name + '/index.html')

@home_app.route(r'/about')
def view_about():
    return render_template(app_name + '/about.html')