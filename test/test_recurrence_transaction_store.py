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

from firefly_iii_client.models.recurrence_transaction_store import RecurrenceTransactionStore

class TestRecurrenceTransactionStore(unittest.TestCase):
    """RecurrenceTransactionStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceTransactionStore:
        """Test RecurrenceTransactionStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceTransactionStore`
        """
        model = RecurrenceTransactionStore()
        if include_optional:
            return RecurrenceTransactionStore(
                amount = '123.45',
                bill_id = '123',
                budget_id = '4',
                category_id = '211',
                currency_code = 'EUR',
                currency_id = '3',
                description = 'Rent for the current month',
                destination_id = '258',
                foreign_amount = '123.45',
                foreign_currency_code = 'GBP',
                foreign_currency_id = '17',
                piggy_bank_id = '123',
                source_id = '913',
                tags = [
                    'Barbecue preparation'
                    ]
            )
        else:
            return RecurrenceTransactionStore(
                amount = '123.45',
                description = 'Rent for the current month',
                destination_id = '258',
                source_id = '913',
        )
        """

    def testRecurrenceTransactionStore(self):
        """Test RecurrenceTransactionStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
