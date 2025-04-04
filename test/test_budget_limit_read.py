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

from firefly_iii_client.models.budget_limit_read import BudgetLimitRead

class TestBudgetLimitRead(unittest.TestCase):
    """BudgetLimitRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetLimitRead:
        """Test BudgetLimitRead
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetLimitRead`
        """
        model = BudgetLimitRead()
        if include_optional:
            return BudgetLimitRead(
                attributes = firefly_iii_client.models.budget_limit.BudgetLimit(
                    amount = '123.45', 
                    budget_id = '23', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_name = 'Euro', 
                    currency_symbol = '$', 
                    end = '2018-09-17T12:46:47+01:00', 
                    native_amount = '123.45', 
                    native_currency_code = 'EUR', 
                    native_currency_decimal_places = 2, 
                    native_currency_id = '5', 
                    native_currency_symbol = '$', 
                    notes = 'Some example notes', 
                    period = 'monthly', 
                    spent = '-1012.12', 
                    start = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                type = 'budget_limits'
            )
        else:
            return BudgetLimitRead(
                attributes = firefly_iii_client.models.budget_limit.BudgetLimit(
                    amount = '123.45', 
                    budget_id = '23', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_name = 'Euro', 
                    currency_symbol = '$', 
                    end = '2018-09-17T12:46:47+01:00', 
                    native_amount = '123.45', 
                    native_currency_code = 'EUR', 
                    native_currency_decimal_places = 2, 
                    native_currency_id = '5', 
                    native_currency_symbol = '$', 
                    notes = 'Some example notes', 
                    period = 'monthly', 
                    spent = '-1012.12', 
                    start = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                type = 'budget_limits',
        )
        """

    def testBudgetLimitRead(self):
        """Test BudgetLimitRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
