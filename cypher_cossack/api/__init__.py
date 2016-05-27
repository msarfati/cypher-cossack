from .cipher import Ciphers


def init_api(api_extension):
    api_extension.add_resource(Ciphers, "/api/ciphers")
    # api_extension.add_resource(author.Author, "/api/ciphers/<str:cipher>")
    # api_extension.add_resource(author.Author, "/api/ciphers/<str:cipher>/encrypt")
    # api_extension.add_resource(author.Author, "/api/ciphers/<str:cipher>/decrypt")
