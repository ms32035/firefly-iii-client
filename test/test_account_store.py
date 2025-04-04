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

from firefly_iii_client.models.account_store import AccountStore

class TestAccountStore(unittest.TestCase):
    """AccountStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountStore:
        """Test AccountStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountStore`
        """
        model = AccountStore()
        if include_optional:
            return AccountStore(
                account_number = '7009312345678',
                account_role = 'defaultAsset',
                active = False,
                bic = 'BOFAUS3N',
                credit_card_type = 'monthlyFull',
                currency_code = 'EUR',
                currency_id = '12',
                iban = 'GB98MIDL07009312345678',
                include_net_worth = True,
                interest = '0',
                interest_period = 'monthly',
                latitude = 51.983333,
                liability_direction = 'credit',
                liability_type = 'loan',
                longitude = 5.916667,
                monthly_payment_date = '2018-09-17T12:46:47+01:00',
                name = 'My checking account',
                notes = 'Some example notes',
                opening_balance = '-1012.12',
                opening_balance_date = '2018-09-17T12:46:47+01:00',
                order = 1,
                type = 'asset',
                virtual_balance = '123.45',
                zoom_level = 6
            )
        else:
            return AccountStore(
                name = 'My checking account',
                type = 'asset',
        )
        """

    def testAccountStore(self):
        """Test AccountStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
