# coding: utf-8

import unittest

from tapioca_mandrill import Mandrill


class TestTapioca(unittest.TestCase):

    def setUp(self):
        self.wrapper = Mandrill(key='random_key')

    def test_access_resource(self):
        resource = self.wrapper.users(method='list')

        self.assertEqual(resource.data(), 'https://mandrillapp.com/api/1.0/users/list.json')



if __name__ == '__main__':
    unittest.main()
