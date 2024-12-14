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

from firefly_iii_client.models.transaction_store import TransactionStore

class TestTransactionStore(unittest.TestCase):
    """TransactionStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionStore:
        """Test TransactionStore
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionStore`
        """
        model = TransactionStore()
        if include_optional:
            return TransactionStore(
                apply_rules = False,
                error_if_duplicate_hash = False,
                fire_webhooks = True,
                group_title = 'Split transaction title.',
                transactions = [
                    firefly_iii_client.models.transaction_split_store.TransactionSplitStore(
                        amount = '123.45', 
                        bill_id = '112', 
                        bill_name = 'Monthly rent', 
                        book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        budget_id = '4', 
                        budget_name = 'Groceries', 
                        bunq_payment_id = '', 
                        category_id = '43', 
                        category_name = 'Groceries', 
                        currency_code = 'EUR', 
                        currency_id = '12', 
                        date = '2018-09-17T12:46:47+01:00', 
                        description = 'Vegetables', 
                        destination_id = '2', 
                        destination_name = 'Buy and Large', 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        external_id = '', 
                        external_url = '', 
                        foreign_amount = '123.45', 
                        foreign_currency_code = 'USD', 
                        foreign_currency_id = '17', 
                        interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        internal_reference = '', 
                        invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        notes = 'Some example notes', 
                        order = 0, 
                        payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        piggy_bank_id = 56, 
                        piggy_bank_name = '', 
                        process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        reconciled = False, 
                        sepa_batch_id = '', 
                        sepa_cc = '', 
                        sepa_ci = '', 
                        sepa_country = '', 
                        sepa_ct_id = '', 
                        sepa_ct_op = '', 
                        sepa_db = '', 
                        sepa_ep = '', 
                        source_id = '2', 
                        source_name = 'Checking account', 
                        tags = [
                            'Barbecue preparation'
                            ], 
                        type = 'withdrawal', )
                    ]
            )
        else:
            return TransactionStore(
                transactions = [
                    firefly_iii_client.models.transaction_split_store.TransactionSplitStore(
                        amount = '123.45', 
                        bill_id = '112', 
                        bill_name = 'Monthly rent', 
                        book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        budget_id = '4', 
                        budget_name = 'Groceries', 
                        bunq_payment_id = '', 
                        category_id = '43', 
                        category_name = 'Groceries', 
                        currency_code = 'EUR', 
                        currency_id = '12', 
                        date = '2018-09-17T12:46:47+01:00', 
                        description = 'Vegetables', 
                        destination_id = '2', 
                        destination_name = 'Buy and Large', 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        external_id = '', 
                        external_url = '', 
                        foreign_amount = '123.45', 
                        foreign_currency_code = 'USD', 
                        foreign_currency_id = '17', 
                        interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        internal_reference = '', 
                        invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        notes = 'Some example notes', 
                        order = 0, 
                        payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        piggy_bank_id = 56, 
                        piggy_bank_name = '', 
                        process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        reconciled = False, 
                        sepa_batch_id = '', 
                        sepa_cc = '', 
                        sepa_ci = '', 
                        sepa_country = '', 
                        sepa_ct_id = '', 
                        sepa_ct_op = '', 
                        sepa_db = '', 
                        sepa_ep = '', 
                        source_id = '2', 
                        source_name = 'Checking account', 
                        tags = [
                            'Barbecue preparation'
                            ], 
                        type = 'withdrawal', )
                    ],
        )
        """

    def testTransactionStore(self):
        """Test TransactionStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
