# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from ...core.database import db


# Base = declarative_base()
Base = db.Model

# 用户-角色-关联
user_role_map = Table('user_role_map', Base.metadata,
    Column('urid', Integer, primary_key=True, autoincrement=True, comment='主键ID'),
    Column('user_id', Integer, ForeignKey('users.uid'), nullable=False, comment='用户ID'),
    Column('role_id', Integer, ForeignKey('roles.rid'), nullable=False, comment='角色ID'),
    UniqueConstraint('user_id', 'role_id')
)

# 角色-权限-关联
role_permission_map = Table('role_permission_map', Base.metadata,
    Column('urid', Integer, primary_key=True, autoincrement=True, comment='主键ID'),
    Column('role_id', Integer, ForeignKey('roles.rid'), nullable=False, comment='角色ID'),
    Column('permission_id', Integer, ForeignKey('permissions.pid'), nullable=False, comment='权限ID'),
    UniqueConstraint('role_id', 'permission_id')
)

class User(Base):
    """用户"""
    __tablename__ = 'users'

    uid = Column('uid', Integer, primary_key=True, autoincrement=True, comment='用户ID')
    email = Column('email', String(250), unique=True, nullable=False, comment='邮箱')
    password = Column('password', String(32), nullable=False, comment='密码')
    nickname = Column('nickname', String(50), nullable=True, comment='昵称')
    register_time = Column(
        'register_time',
        DateTime(timezone=True),
        default=datetime.now(tz=pytz.timezone('Asia/Shanghai')),
        comment='注册时间'
    )

    roles = relationship('Role',
        secondary=user_role_map,
        backref=backref('users', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, email, password, nickname=None):
        self.email = email
        self.password = password
        self.nickname = nickname

    def __repr__(self):
        return '<{0} {1!r}>'.format(__class__.__name__, self.email)

class Role(Base):
    """角色"""
    __tablename__ = 'roles'
    
    rid = Column('rid', Integer, primary_key=True, autoincrement=True, comment='角色ID')
    name = Column('name', String(50), unique=True, nullable=False, comment='角色名')

    permissions = relationship('Permission',
        secondary=role_permission_map,
        backref=backref('roles', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<{0} {1!r}>'.format(__class__.__name__, self.name)

class Permission(Base):
    """权限"""
    __tablename__ = 'permissions'
    __table_args__ = (
        UniqueConstraint('name', 'endpoint'),
    )
    
    pid = Column('pid', Integer, primary_key=True, autoincrement=True, comment='权限ID')
    name = Column('name', String(50), unique=True, nullable=False, comment='权限名')
    endpoint = Column('endpoint', String(250), unique=True, nullable=False, comment='权限操作挂载的路由')

    def __init__(self, endpoint, name):
        self.endpoint = endpoint
        self.name = name

    def to_dict(self):
        return {
            'pid': self.pid,
            'name': self.name,
            'endpoint': self.endpoint
        }

    def __repr__(self):
        return '<{0} {1!r}>'.format(__class__.__name__, self.name)