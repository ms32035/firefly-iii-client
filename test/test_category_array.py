# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 6.1.24
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.models.category_array import CategoryArray

class TestCategoryArray(unittest.TestCase):
    """CategoryArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryArray:
        """Test CategoryArray
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryArray`
        """
        model = CategoryArray()
        if include_optional:
            return CategoryArray(
                data = [
                    firefly_iii_client.models.category_read.CategoryRead(
                        attributes = firefly_iii_client.models.category.Category(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            earned = [
                                firefly_iii_client.models.category_earned.CategoryEarned(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '123.45', )
                                ], 
                            name = 'Lunch', 
                            notes = 'Some example notes', 
                            spent = [
                                firefly_iii_client.models.category_spent.CategorySpent(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '-12423.45', )
                                ], 
                            updated_at = '2018-09-17T12:46:47+01:00', ), 
                        id = '2', 
                        type = 'categories', )
                    ],
                meta = firefly_iii_client.models.meta.Meta(
                    pagination = firefly_iii_client.models.meta_pagination.Meta_pagination(
                        count = 20, 
                        current_page = 1, 
                        per_page = 100, 
                        total = 3, 
                        total_pages = 1, ), )
            )
        else:
            return CategoryArray(
                data = [
                    firefly_iii_client.models.category_read.CategoryRead(
                        attributes = firefly_iii_client.models.category.Category(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            earned = [
                                firefly_iii_client.models.category_earned.CategoryEarned(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '123.45', )
                                ], 
                            name = 'Lunch', 
                            notes = 'Some example notes', 
                            spent = [
                                firefly_iii_client.models.category_spent.CategorySpent(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '-12423.45', )
                                ], 
                            updated_at = '2018-09-17T12:46:47+01:00', ), 
                        id = '2', 
                        type = 'categories', )
                    ],
                meta = firefly_iii_client.models.meta.Meta(
                    pagination = firefly_iii_client.models.meta_pagination.Meta_pagination(
                        count = 20, 
                        current_page = 1, 
                        per_page = 100, 
                        total = 3, 
                        total_pages = 1, ), ),
        )
        """

    def testCategoryArray(self):
        """Test CategoryArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
