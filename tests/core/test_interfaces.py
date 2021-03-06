from unittest import TestCase

from apps.core.interfaces import APIModel


class DummyAPIModel(APIModel):
    pass


class APIModelTestCase(TestCase):
    def test_raise_attr_error(self):
        m = DummyAPIModel({"heyho": 1})
        assert 1 == m.heyho
        with self.assertRaises(AttributeError):
            assert m.wobble
