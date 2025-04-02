# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: v6.2.10
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.models.user_array import UserArray

class TestUserArray(unittest.TestCase):
    """UserArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserArray:
        """Test UserArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserArray`
        """
        model = UserArray()
        if include_optional:
            return UserArray(
                data = [
                    firefly_iii_client.models.user_read.UserRead(
                        attributes = firefly_iii_client.models.a_single_user.A single user(
                            blocked = False, 
                            blocked_code = 'email_changed', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            email = 'james@firefly-iii.org', 
                            role = 'owner', 
                            updated_at = '2018-09-17T12:46:47+01:00', ), 
                        id = '2', 
                        links = firefly_iii_client.models.object_link.ObjectLink(
                            0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), 
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                        type = 'users', )
                    ],
                links = firefly_iii_client.models.page_link.PageLink(
                    first = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=1', 
                    last = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=12', 
                    next = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=3', 
                    prev = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=2', 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=4', ),
                meta = firefly_iii_client.models.meta.Meta(
                    pagination = firefly_iii_client.models.meta_pagination.Meta_pagination(
                        count = 20, 
                        current_page = 1, 
                        per_page = 100, 
                        total = 3, 
                        total_pages = 1, ), )
            )
        else:
            return UserArray(
                data = [
                    firefly_iii_client.models.user_read.UserRead(
                        attributes = firefly_iii_client.models.a_single_user.A single user(
                            blocked = False, 
                            blocked_code = 'email_changed', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            email = 'james@firefly-iii.org', 
                            role = 'owner', 
                            updated_at = '2018-09-17T12:46:47+01:00', ), 
                        id = '2', 
                        links = firefly_iii_client.models.object_link.ObjectLink(
                            0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), 
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                        type = 'users', )
                    ],
                links = firefly_iii_client.models.page_link.PageLink(
                    first = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=1', 
                    last = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=12', 
                    next = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=3', 
                    prev = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=2', 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=4', ),
                meta = firefly_iii_client.models.meta.Meta(
                    pagination = firefly_iii_client.models.meta_pagination.Meta_pagination(
                        count = 20, 
                        current_page = 1, 
                        per_page = 100, 
                        total = 3, 
                        total_pages = 1, ), ),
        )
        """

    def testUserArray(self):
        """Test UserArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
