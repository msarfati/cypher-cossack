from ..mixins import TestCaseMixin
from nose.plugins.attrib import attr
import json


class CiphersTestCase(TestCaseMixin):

    @attr('single')
    def test_get(self):
        "Testing api.Ciphers.get"
        r = self.client.get("/api/ciphers")
        self.assertEquals(r.status_code, 200)
        # import ipdb; ipdb.set_trace()
        # self.assertEquals(r.status_code, 404)
