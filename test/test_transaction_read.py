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

from firefly_iii_client.models.transaction_read import TransactionRead

class TestTransactionRead(unittest.TestCase):
    """TransactionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRead:
        """Test TransactionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRead`
        """
        model = TransactionRead()
        if include_optional:
            return TransactionRead(
                attributes = firefly_iii_client.models.transaction.Transaction(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    group_title = 'Split transaction title.', 
                    transactions = [
                        firefly_iii_client.models.transaction_split.TransactionSplit(
                            amount = '123.45', 
                            bill_id = '111', 
                            bill_name = 'Monthly rent', 
                            book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            budget_id = '4', 
                            budget_name = 'Groceries', 
                            bunq_payment_id = '', 
                            category_id = '43', 
                            category_name = 'Groceries', 
                            currency_code = 'EUR', 
                            currency_decimal_places = 2, 
                            currency_id = '12', 
                            currency_name = 'Euro', 
                            currency_symbol = '$', 
                            date = '2018-09-17T12:46:47+01:00', 
                            description = 'Vegetables', 
                            destination_iban = 'NL02ABNA0123456789', 
                            destination_id = '2', 
                            destination_name = 'Buy and Large', 
                            destination_type = 'Asset account', 
                            due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            external_id = '', 
                            external_url = '', 
                            foreign_amount = '123.45', 
                            foreign_currency_code = 'USD', 
                            foreign_currency_decimal_places = 2, 
                            foreign_currency_id = '17', 
                            foreign_currency_symbol = '$', 
                            has_attachments = False, 
                            import_hash_v2 = '', 
                            interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            internal_reference = '', 
                            invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = 51.983333, 
                            longitude = 5.916667, 
                            notes = 'Some example notes', 
                            order = 0, 
                            original_source = '', 
                            payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reconciled = False, 
                            recurrence_count = 12, 
                            recurrence_id = '', 
                            recurrence_total = 0, 
                            sepa_batch_id = '', 
                            sepa_cc = '', 
                            sepa_ci = '', 
                            sepa_country = '', 
                            sepa_ct_id = '', 
                            sepa_ct_op = '', 
                            sepa_db = '', 
                            sepa_ep = '', 
                            source_iban = 'NL02ABNA0123456789', 
                            source_id = '2', 
                            source_name = 'Checking account', 
                            source_type = 'Asset account', 
                            tags = [
                                'Barbecue preparation'
                                ], 
                            transaction_journal_id = '10421', 
                            type = 'withdrawal', 
                            user = '3', 
                            zoom_level = 6, )
                        ], 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    user = '3', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'transactions'
            )
        else:
            return TransactionRead(
                attributes = firefly_iii_client.models.transaction.Transaction(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    group_title = 'Split transaction title.', 
                    transactions = [
                        firefly_iii_client.models.transaction_split.TransactionSplit(
                            amount = '123.45', 
                            bill_id = '111', 
                            bill_name = 'Monthly rent', 
                            book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            budget_id = '4', 
                            budget_name = 'Groceries', 
                            bunq_payment_id = '', 
                            category_id = '43', 
                            category_name = 'Groceries', 
                            currency_code = 'EUR', 
                            currency_decimal_places = 2, 
                            currency_id = '12', 
                            currency_name = 'Euro', 
                            currency_symbol = '$', 
                            date = '2018-09-17T12:46:47+01:00', 
                            description = 'Vegetables', 
                            destination_iban = 'NL02ABNA0123456789', 
                            destination_id = '2', 
                            destination_name = 'Buy and Large', 
                            destination_type = 'Asset account', 
                            due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            external_id = '', 
                            external_url = '', 
                            foreign_amount = '123.45', 
                            foreign_currency_code = 'USD', 
                            foreign_currency_decimal_places = 2, 
                            foreign_currency_id = '17', 
                            foreign_currency_symbol = '$', 
                            has_attachments = False, 
                            import_hash_v2 = '', 
                            interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            internal_reference = '', 
                            invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = 51.983333, 
                            longitude = 5.916667, 
                            notes = 'Some example notes', 
                            order = 0, 
                            original_source = '', 
                            payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reconciled = False, 
                            recurrence_count = 12, 
                            recurrence_id = '', 
                            recurrence_total = 0, 
                            sepa_batch_id = '', 
                            sepa_cc = '', 
                            sepa_ci = '', 
                            sepa_country = '', 
                            sepa_ct_id = '', 
                            sepa_ct_op = '', 
                            sepa_db = '', 
                            sepa_ep = '', 
                            source_iban = 'NL02ABNA0123456789', 
                            source_id = '2', 
                            source_name = 'Checking account', 
                            source_type = 'Asset account', 
                            tags = [
                                'Barbecue preparation'
                                ], 
                            transaction_journal_id = '10421', 
                            type = 'withdrawal', 
                            user = '3', 
                            zoom_level = 6, )
                        ], 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    user = '3', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'transactions',
        )
        """

    def testTransactionRead(self):
        """Test TransactionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
