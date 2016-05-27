from ..mixins import TestCaseMixin
from nose.plugins.attrib import attr
import json


class CiphersTestCase(TestCaseMixin):

    # @attr('single')
    def test_get(self):
        "Testing api.Ciphers.get"
        r = self.client.get("/api/ciphers")
        self.assertEquals(r.status_code, 200)
        self.assertGreaterEqual(len(r.json['ciphers']), 2, "Payload serializable.")


class CipherTestCase(TestCaseMixin):

    # @attr('single')
    def test_get(self):
        "Testing api.Cipher.get"
        r = self.client.get("/api/ciphers")
        r = self.client.get("/api/ciphers/" + r.json['ciphers'][0])
        self.assertEquals(r.status_code, 200)
        self.assertGreaterEqual(len(r.json), 3, "Payload serializable.")
