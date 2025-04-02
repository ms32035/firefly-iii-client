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

from firefly_iii_client.models.rule_trigger import RuleTrigger

class TestRuleTrigger(unittest.TestCase):
    """RuleTrigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleTrigger:
        """Test RuleTrigger
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleTrigger`
        """
        model = RuleTrigger()
        if include_optional:
            return RuleTrigger(
                active = True,
                created_at = '2018-09-17T12:46:47+01:00',
                id = '2',
                order = 5,
                prohibited = False,
                stop_processing = False,
                type = 'user_action',
                updated_at = '2018-09-17T12:46:47+01:00',
                value = 'tag1'
            )
        else:
            return RuleTrigger(
                type = 'user_action',
                value = 'tag1',
        )
        """

    def testRuleTrigger(self):
        """Test RuleTrigger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
