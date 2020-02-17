#coding=utf-8
'''
Created on 2020-02-07

@author: jianzhihua

@attention:
'''
import json
from flask_restful import Resource
from flask_restful import request


class BaseHandler(Resource):

    @property
    def params(self):
        data = {}
        if request.method in ("POST", "PUT"):
            data = request.get_json(force=True)
        elif request.method in ("DELETE", "GET"):
            for ud in request.args.items():
                data[ud[0]] = ud[1]
        setattr(request, 'bjson', data)
        return data

