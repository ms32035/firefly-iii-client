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

from firefly_iii_client.models.piggy_bank_single import PiggyBankSingle

class TestPiggyBankSingle(unittest.TestCase):
    """PiggyBankSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PiggyBankSingle:
        """Test PiggyBankSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PiggyBankSingle`
        """
        model = PiggyBankSingle()
        if include_optional:
            return PiggyBankSingle(
                data = firefly_iii_client.models.piggy_bank_read.PiggyBankRead(
                    attributes = firefly_iii_client.models.piggy_bank.PiggyBank(
                        accounts = [
                            firefly_iii_client.models.piggy_bank_account_read.PiggyBankAccountRead(
                                current_amount = '123.45', 
                                id = '3', 
                                name = 'Checking account', 
                                native_current_amount = '123.45', )
                            ], 
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
                    type = 'piggy_banks', )
            )
        else:
            return PiggyBankSingle(
                data = firefly_iii_client.models.piggy_bank_read.PiggyBankRead(
                    attributes = firefly_iii_client.models.piggy_bank.PiggyBank(
                        accounts = [
                            firefly_iii_client.models.piggy_bank_account_read.PiggyBankAccountRead(
                                current_amount = '123.45', 
                                id = '3', 
                                name = 'Checking account', 
                                native_current_amount = '123.45', )
                            ], 
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
                    type = 'piggy_banks', ),
        )
        """

    def testPiggyBankSingle(self):
        """Test PiggyBankSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
