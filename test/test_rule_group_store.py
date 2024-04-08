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

from firefly_iii_client.models.rule_group_store import RuleGroupStore

class TestRuleGroupStore(unittest.TestCase):
    """RuleGroupStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleGroupStore:
        """Test RuleGroupStore
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleGroupStore`
        """
        model = RuleGroupStore()
        if include_optional:
            return RuleGroupStore(
                active = True,
                description = 'Description of this rule group',
                order = 4,
                title = 'Default rule group'
            )
        else:
            return RuleGroupStore(
                title = 'Default rule group',
        )
        """

    def testRuleGroupStore(self):
        """Test RuleGroupStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
