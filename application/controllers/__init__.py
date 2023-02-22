#!/usr/bin/env python
# encoding: utf-8
from application.controllers import auth
from application.controllers import user
from application.controllers import todo

all_bp = [
    auth.auth_bp,
    user.user_bp,
    todo.todo_bp
]
