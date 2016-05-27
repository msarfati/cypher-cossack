from .cipher import Ciphers, Cipher, CipherEncrypt


def init_api(api_extension):
    api_extension.add_resource(Ciphers, "/api/ciphers")
    api_extension.add_resource(Cipher, "/api/ciphers/<cipher>")
    api_extension.add_resource(CipherEncrypt, "/api/ciphers/<cipher>/encrypt")
    # api_extension.add_resource(author.Author, "/api/ciphers/<str:cipher>/decrypt")
