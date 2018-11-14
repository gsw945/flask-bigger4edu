# -*- coding: utf-8 -*-
'''（子）应用路径映射'''
from .apps.home.main import home_app


blueprints = [
    ('', home_app)
]