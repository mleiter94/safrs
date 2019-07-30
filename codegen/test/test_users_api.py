# coding: utf-8

"""
    SAFRS Demo App

    <a href=http://jsonapi.org>Json-API</a> compliant API built with https://github.com/thomaxxl/safrs <br/>- <a href=\"https://github.com/thomaxxl/safrs/blob/master/examples/demo_relationship.py\">Source code of this page</a> <br/> - Auto-generated swagger spec: <a href=swagger.json>swagger.json</a> <br/> - Petstore <a href=http://petstore.swagger.io/?url=http://thomaxxl.pythonanywhere.com/api/swagger.json>Swagger2 UI</a>                                         # noqa: E501

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_1(self):
        """Test case for 1

        Retrieve a User object              # noqa: E501
        """
        pass

    def test_1_0(self):
        """Test case for 1_0

        Create a User object              # noqa: E501
        """
        pass

    def test_1_1(self):
        """Test case for 1_1

        Delete a User object              # noqa: E501
        """
        pass

    def test_1_2(self):
        """Test case for 1_2

        Update a User object              # noqa: E501
        """
        pass

    def test_2(self):
        """Test case for 2

        Retrieve a User object                          # noqa: E501
        """
        pass

    def test_2_0(self):
        """Test case for 2_0

        Create a User object                          # noqa: E501
        """
        pass

    def test_2_1(self):
        """Test case for 2_1

        Delete from User books  # noqa: E501
        """
        pass

    def test_3(self):
        """Test case for 3

        Retrieve a books object  # noqa: E501
        """
        pass

    def test_3_0(self):
        """Test case for 3_0

        Update books  # noqa: E501
        """
        pass

    def test_4(self):
        """Test case for 4

        Invoke User.get_list              # noqa: E501
        """
        pass

    def test_4_0(self):
        """Test case for 4_0

        Retrieve a books object  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
