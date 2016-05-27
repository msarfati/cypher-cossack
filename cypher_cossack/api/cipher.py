from .. import cipher as cipher_alg
from flask import jsonify, url_for
from flask.ext.restful import abort, Api, Resource, reqparse, fields, marshal

cipher_alg_lookup = {
    "rc4": {
        "_algorithm": cipher_alg.RC4,
        "name": "rc4",
        "other_names": ['Rivest Cipher 4', 'ARC4', 'ARCFOUR'],
        "wiki": "https://en.wikipedia.org/wiki/RC4",
    },
    "tea": {
        "_algorithm": None,
        "name": "tea",
        "other_names": ['Tiny Encryption Algorithm'],
        "wiki": "https://en.wikipedia.org/wiki/Tiny_Encryption_Algorithm",
    }
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
            return jsonify(ciphers=[*cipher_alg_lookup.keys()])
        except:
            abort(404)

    def post(self):
        pass


class Cipher(Resource):
    """
    Operations dealing with individual ciphers
    """
    # decorators = [auth.login_required]

    def get(self, cipher):
        # import ipdb; ipdb.set_trace()
        try:
            cipher = cipher_alg_lookup[cipher]
        except:
            return abort(404, message="'{}' is invalid. Please get the current list of ciphers".format(cipher), rel=url_for(Ciphers.get))

        try:
            # import ipdb; ipdb.set_trace()
            return jsonify(**{k: v for k, v in cipher.items() if k[0] is not "_"})
        except:
            abort(404)


# class CipherEncrypt(Resource):
#     """
#     Operations dealing with individual ciphers
#     """
#     # decorators = [auth.login_required]

#     def post(self, cipher):
#         # import ipdb; ipdb.set_trace()
#         try:
#             cipher = cipher_alg_lookup[cipher]
#         except:
#             return abort(404, message="'{}' is invalid. Please get the current list of ciphers".format(cipher), rel=url_for(Ciphers.get))

#         try:
#             # import ipdb; ipdb.set_trace()
#             return jsonify(**{k: v for k, v in cipher.items() if k[0] is not "_"})
#         except:
#             abort(404)


# class CipherEncrypt(Resource):
#     """
#     Operations dealing with individual ciphers
#     """
#     # decorators = [auth.login_required]

#     def post(self, cipher):
#         # import ipdb; ipdb.set_trace()
#         try:
#             cipher = cipher_alg_lookup[cipher]
#         except:
#             return abort(404, message="'{}' is invalid. Please get the current list of ciphers".format(cipher), rel=url_for(Ciphers.get))

#         try:
#             # import ipdb; ipdb.set_trace()
#             return jsonify(**{k: v for k, v in cipher.items() if k[0] is not "_"})
#         except:
#             abort(404)
