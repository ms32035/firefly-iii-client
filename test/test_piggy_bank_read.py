# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.models.piggy_bank_read import PiggyBankRead

class TestPiggyBankRead(unittest.TestCase):
    """PiggyBankRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PiggyBankRead:
        """Test PiggyBankRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PiggyBankRead`
        """
        model = PiggyBankRead()
        if include_optional:
            return PiggyBankRead(
                attributes = firefly_iii_client.models.piggy_bank.PiggyBank(
                    account_id = '13', 
                    account_name = 'Savings account', 
                    active = True, 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'USD', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    current_amount = '123.45', 
                    left_to_save = '700.00', 
                    name = 'New digital camera', 
                    notes = 'Some notes', 
                    object_group_id = '5', 
                    object_group_order = 5, 
                    object_group_title = 'Example Group', 
                    order = 5, 
                    percentage = 12.5, 
                    save_per_month = '12.45', 
                    start_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                    target_amount = '123.45', 
                    target_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'piggy_banks'
            )
        else:
            return PiggyBankRead(
                attributes = firefly_iii_client.models.piggy_bank.PiggyBank(
                    account_id = '13', 
                    account_name = 'Savings account', 
                    active = True, 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'USD', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    current_amount = '123.45', 
                    left_to_save = '700.00', 
                    name = 'New digital camera', 
                    notes = 'Some notes', 
                    object_group_id = '5', 
                    object_group_order = 5, 
                    object_group_title = 'Example Group', 
                    order = 5, 
                    percentage = 12.5, 
                    save_per_month = '12.45', 
                    start_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                    target_amount = '123.45', 
                    target_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'piggy_banks',
        )
        """

    def testPiggyBankRead(self):
        """Test PiggyBankRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
