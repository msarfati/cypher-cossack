from ..mixins import TestCaseMixin
from . import fixtures
from nose.plugins.attrib import attr


class RC4TestCase(TestCaseMixin):

    @attr('single')
    def test_testing(self):
        self.assertEqual(2, 1+1)
