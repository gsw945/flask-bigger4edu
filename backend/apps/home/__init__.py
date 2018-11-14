# -*- coding: utf-8 -*-
'''站点首页-后端'''
from flask import Blueprint

from .. import (
    template_folder,
    static_folder,
    static_url_prefix
)
from ...app_env import get_config


'''
# 直接从上层包提取，此处不用提取了
env_cfg = get_config()
template_folder = env_cfg.get('template_folder', None)
static_folder = env_cfg.get('static_folder', None)
static_url_prefix = env_cfg.get('static_url_prefix', None)
'''


app_name = 'home'
home_app = Blueprint(
    app_name,
    __name__,
    static_folder=template_folder,
    template_folder=static_folder,
    static_url_path=static_url_prefix
)