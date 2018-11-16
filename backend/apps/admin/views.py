# -*- coding: utf-8 -*-
'''站点首页视图'''
from flask import render_template

from . import admin_app, app_name


@admin_app.route('/')
def view_index():
    return render_template(app_name + '/pages/index.html', page_id='view-index')

@admin_app.route('/test/blank')
def view_test_blank():
    return render_template(app_name + '/pages/test-blank.html', page_id='view-test-blank')

@admin_app.route('/auth/login')
def view_auth_login():
    return render_template(app_name + '/pages/auth-login.html', page_id='view-auth-login')

@admin_app.route('/auth/retrieve')
def view_auth_retrieve():
    return render_template(app_name + '/pages/auth-retrieve.html', page_id='view-auth-retrieve')