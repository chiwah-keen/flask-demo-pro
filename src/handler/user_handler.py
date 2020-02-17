#coding=utf-8
'''
Created on 2020-02-07

@author: jianzhihua

@attention:
'''
from handler.base_handler import BaseHandler
import utils.custom_response as cr
from services.jwt_operator import is_login, create_jwt_token
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_jwt_extended import get_current_user
from utils.custom_mark import TipResponse


class UserHandler(BaseHandler):

    def post(self):
        params = self.params
        token = create_jwt_token(user_id=123)
        return cr.op_success(data=token)

    @is_login
    def put(self):
        params = self.params
        a = get_current_user()
        raise TipResponse("123456")
