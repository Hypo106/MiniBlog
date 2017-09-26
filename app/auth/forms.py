#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File Name is forms.py
# Created by Hypo.Wang at 2017/9/26 16:32

from flask_wtf import Form
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    email = StringField(u'电子邮件', validators=[DataRequired(),
                                             Length(1,64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])