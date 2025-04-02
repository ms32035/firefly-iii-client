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

from firefly_iii_client.models.available_budget_array import AvailableBudgetArray

class TestAvailableBudgetArray(unittest.TestCase):
    """AvailableBudgetArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvailableBudgetArray:
        """Test AvailableBudgetArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvailableBudgetArray`
        """
        model = AvailableBudgetArray()
        if include_optional:
            return AvailableBudgetArray(
                data = [
                    firefly_iii_client.models.available_budget_read.AvailableBudgetRead(
                        attributes = firefly_iii_client.models.available_budget.AvailableBudget(
                            amount = '123.45', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            currency_code = 'EUR', 
                            currency_decimal_places = 2, 
                            currency_id = '5', 
                            currency_symbol = '$', 
                            end = '2018-09-17T12:46:47+01:00', 
                            native_amount = '123.45', 
                            native_currency_code = 'EUR', 
                            native_currency_decimal_places = 2, 
                            native_currency_id = '5', 
                            native_currency_symbol = '$', 
                            spent_in_budgets = [
                                firefly_iii_client.models.budget_spent.BudgetSpent(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '123.45', )
                                ], 
                            spent_outside_budget = [
                                firefly_iii_client.models.budget_spent.BudgetSpent(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '123.45', )
                                ], 
                            start = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', ), 
                        id = '2', 
                        type = 'available_budgets', )
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
            return AvailableBudgetArray(
                data = [
                    firefly_iii_client.models.available_budget_read.AvailableBudgetRead(
                        attributes = firefly_iii_client.models.available_budget.AvailableBudget(
                            amount = '123.45', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            currency_code = 'EUR', 
                            currency_decimal_places = 2, 
                            currency_id = '5', 
                            currency_symbol = '$', 
                            end = '2018-09-17T12:46:47+01:00', 
                            native_amount = '123.45', 
                            native_currency_code = 'EUR', 
                            native_currency_decimal_places = 2, 
                            native_currency_id = '5', 
                            native_currency_symbol = '$', 
                            spent_in_budgets = [
                                firefly_iii_client.models.budget_spent.BudgetSpent(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '123.45', )
                                ], 
                            spent_outside_budget = [
                                firefly_iii_client.models.budget_spent.BudgetSpent(
                                    currency_code = 'USD', 
                                    currency_decimal_places = 2, 
                                    currency_id = '5', 
                                    currency_symbol = '$', 
                                    sum = '123.45', )
                                ], 
                            start = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', ), 
                        id = '2', 
                        type = 'available_budgets', )
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

    def testAvailableBudgetArray(self):
        """Test AvailableBudgetArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
