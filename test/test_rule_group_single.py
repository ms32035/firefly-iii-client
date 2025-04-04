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

from firefly_iii_client.models.rule_group_single import RuleGroupSingle

class TestRuleGroupSingle(unittest.TestCase):
    """RuleGroupSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleGroupSingle:
        """Test RuleGroupSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleGroupSingle`
        """
        model = RuleGroupSingle()
        if include_optional:
            return RuleGroupSingle(
                data = firefly_iii_client.models.rule_group_read.RuleGroupRead(
                    attributes = firefly_iii_client.models.rule_group.RuleGroup(
                        active = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        description = 'Description of this rule group', 
                        order = 4, 
                        title = 'Default rule group', 
                        updated_at = '2018-09-17T12:46:47+01:00', ), 
                    id = '2', 
                    links = firefly_iii_client.models.object_link.ObjectLink(
                        0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                    type = 'rules_group', )
            )
        else:
            return RuleGroupSingle(
                data = firefly_iii_client.models.rule_group_read.RuleGroupRead(
                    attributes = firefly_iii_client.models.rule_group.RuleGroup(
                        active = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        description = 'Description of this rule group', 
                        order = 4, 
                        title = 'Default rule group', 
                        updated_at = '2018-09-17T12:46:47+01:00', ), 
                    id = '2', 
                    links = firefly_iii_client.models.object_link.ObjectLink(
                        0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                    type = 'rules_group', ),
        )
        """

    def testRuleGroupSingle(self):
        """Test RuleGroupSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
