#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column



class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_exists(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, 'state_id'))

    def test_name_exists(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, 'name'))

    def test_inherits_from_Base(self):
        """ """
        new = self.value()
        self.assertIsInstance(new, Base)
