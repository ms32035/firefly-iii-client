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

from firefly_iii_client.models.recurrence_repetition_store import RecurrenceRepetitionStore

class TestRecurrenceRepetitionStore(unittest.TestCase):
    """RecurrenceRepetitionStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceRepetitionStore:
        """Test RecurrenceRepetitionStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceRepetitionStore`
        """
        model = RecurrenceRepetitionStore()
        if include_optional:
            return RecurrenceRepetitionStore(
                moment = '3',
                skip = 0,
                type = 'weekly',
                weekend = 1
            )
        else:
            return RecurrenceRepetitionStore(
                moment = '3',
                type = 'weekly',
        )
        """

    def testRecurrenceRepetitionStore(self):
        """Test RecurrenceRepetitionStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
