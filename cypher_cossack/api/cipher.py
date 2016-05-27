from .. import cipher as cipher_alg
from flask import jsonify, url_for
from flask.ext.restful import abort, Api, Resource, reqparse, fields, marshal

cipher_alg_lookup = {
    "rc4": {
            "algorithm": cipher_alg.RC4,
            "wiki": "https://en.wikipedia.org/wiki/RC4",
        },
}


class Ciphers(Resource):
    """
    Operations dealing with all ciphers
    """
    # decorators = [auth.login_required]

    def get(self):
        """
        Returns a list of currently supported ciphers.
        """
        try:
            return jsonify([*cipher_alg_lookup.keys()])
        except:
            abort(404)

    def post(self):
        pass


# class Cipher(Resource):
#     """
#     Operations dealing with individual ciphers
#     """
#     # decorators = [auth.login_required]

#     def get(self, name):
#         # import ipdb; ipdb.set_trace()
#         obj = models.Author.query.filter(models.Author.id == id).first()
#         try:
#             return jsonify(**obj.dump())
#         except:
#             abort(404)

#     def put(self, id):
#         args = get_Author_args(required=True)
#         author = models.Author.query.filter(models.Author.id == id).first()
#         if author:
#             author.name = args['name']
#             author.pos = args['pos']
#             db.session.add(author)
#             db.session.commit()
#             return json.dumps(author.as_dict())

#     def delete(self, id):
#         obj = models.Clinic.find(id=id)
#         if obj:
#             return obj.delete()
#         else:
#             abort(404, message="object does not exist")

