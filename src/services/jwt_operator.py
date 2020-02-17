#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020年02月10日

@author: jianzhihua
'''

from functools import wraps
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims, verify_jwt_in_request, get_current_user
)
from initialization.jwtextend_process import main_jwt
from utils.custom_mark import TipResponse


def is_login(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        user = get_current_user()
        if not claims or 'ut' not in claims or claims['ut'] != "0":
            raise TipResponse('Illlegal Authorization!')
        if not user:
            raise TipResponse('Not login!')
        else:
            return fn(*args, **kwargs)
    return wrapper


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what custom claims
# should be added to the access token.
# user get_jwt_claims() function will get the result.
@main_jwt.user_claims_loader
def add_claims_to_access_token(identify):
    return {
        'uid': identify,
        'ut': '0'
    }


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what the identity
# of the access token should be.
# user get_jwt_identity()  function will get the result.
@main_jwt.user_identity_loader
def user_identity_lookup(identify):
    return identify


@main_jwt.unauthorized_loader
def request_unauthorized(errmsg):
    raise TipResponse(errmsg)


@main_jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    msg='The {} token has expired'.format(token_type)
    raise TipResponse(msg)


@main_jwt.user_loader_callback_loader
def user_loader_callback(identity):
    user = {"100": 100, "200": identity}
    if not user: return None
    return user


def create_jwt_token(user_id):
    return create_access_token(str(user_id))