import app
import unittest as ut
import json


class AppTestCase(ut.TestCase):

    def setUp(self):
        print("==> Setting up test env.")
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        print("==> Tearing down test env.")
