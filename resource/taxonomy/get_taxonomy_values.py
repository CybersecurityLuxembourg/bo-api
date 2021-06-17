from flask_restful import Resource
from flask_apispec import MethodResource
from flask_jwt_extended import jwt_required
from decorator.catch_exception import catch_exception
from decorator.verify_admin_access import verify_admin_access
from utils.serializer import Serializer
from flask import request
from decorator.log_request import log_request
from webargs import fields
from flask_apispec import use_kwargs, doc


class GetTaxonomyValues(MethodResource, Resource):

    def __init__(self, db):
        self.db = db

    @log_request
    @doc(tags=['taxonomy'],
         description='Get all the taxonomy values',
         responses={
             "200": {},
         })
    @use_kwargs({
        'category': fields.Str(required=False),
    })
    @jwt_required
    @verify_admin_access
    @catch_exception
    def get(self, **kwargs):

        data = self.db.get(self.db.tables["TaxonomyValue"], kwargs)
        data = Serializer.serialize(data, self.db.tables["TaxonomyValue"])

        return data, "200 "
