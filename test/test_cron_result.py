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

from firefly_iii_client.models.cron_result import CronResult

class TestCronResult(unittest.TestCase):
    """CronResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CronResult:
        """Test CronResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CronResult`
        """
        model = CronResult()
        if include_optional:
            return CronResult(
                auto_budgets = firefly_iii_client.models.cron_result_row.CronResultRow(
                    job_errored = False, 
                    job_fired = True, 
                    job_succeeded = True, 
                    message = 'Cron result message', ),
                recurring_transactions = firefly_iii_client.models.cron_result_row.CronResultRow(
                    job_errored = False, 
                    job_fired = True, 
                    job_succeeded = True, 
                    message = 'Cron result message', ),
                telemetry = firefly_iii_client.models.cron_result_row.CronResultRow(
                    job_errored = False, 
                    job_fired = True, 
                    job_succeeded = True, 
                    message = 'Cron result message', )
            )
        else:
            return CronResult(
        )
        """

    def testCronResult(self):
        """Test CronResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
