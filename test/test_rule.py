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

from firefly_iii_client.models.rule import Rule

class TestRule(unittest.TestCase):
    """Rule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Rule:
        """Test Rule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Rule`
        """
        model = Rule()
        if include_optional:
            return Rule(
                actions = [
                    firefly_iii_client.models.rule_action.RuleAction(
                        active = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        id = '2', 
                        order = 5, 
                        stop_processing = False, 
                        type = 'set_category', 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        value = 'Daily groceries', )
                    ],
                active = True,
                created_at = '2018-09-17T12:46:47+01:00',
                description = 'First rule description',
                order = 5,
                rule_group_id = '81',
                rule_group_title = 'New rule group',
                stop_processing = False,
                strict = True,
                title = 'First rule title.',
                trigger = 'store-journal',
                triggers = [
                    firefly_iii_client.models.rule_trigger.RuleTrigger(
                        active = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        id = '2', 
                        order = 5, 
                        stop_processing = False, 
                        type = 'user_action', 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        value = 'tag1', )
                    ],
                updated_at = '2018-09-17T12:46:47+01:00'
            )
        else:
            return Rule(
                actions = [
                    firefly_iii_client.models.rule_action.RuleAction(
                        active = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        id = '2', 
                        order = 5, 
                        stop_processing = False, 
                        type = 'set_category', 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        value = 'Daily groceries', )
                    ],
                rule_group_id = '81',
                title = 'First rule title.',
                trigger = 'store-journal',
                triggers = [
                    firefly_iii_client.models.rule_trigger.RuleTrigger(
                        active = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        id = '2', 
                        order = 5, 
                        stop_processing = False, 
                        type = 'user_action', 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        value = 'tag1', )
                    ],
        )
        """

    def testRule(self):
        """Test Rule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
