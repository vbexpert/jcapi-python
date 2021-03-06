# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv2
from jcapiv2.api.workday_import_api import WorkdayImportApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestWorkdayImportApi(unittest.TestCase):
    """WorkdayImportApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.workday_import_api.WorkdayImportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_workdays_authorize(self):
        """Test case for workdays_authorize

        Authorize Workday  # noqa: E501
        """
        pass

    def test_workdays_deauthorize(self):
        """Test case for workdays_deauthorize

        Deauthorize Workday  # noqa: E501
        """
        pass

    def test_workdays_delete(self):
        """Test case for workdays_delete

        Delete Workday  # noqa: E501
        """
        pass

    def test_workdays_get(self):
        """Test case for workdays_get

        Get Workday  # noqa: E501
        """
        pass

    def test_workdays_import(self):
        """Test case for workdays_import

        Workday Import  # noqa: E501
        """
        pass

    def test_workdays_importresults(self):
        """Test case for workdays_importresults

        List Import Results  # noqa: E501
        """
        pass

    def test_workdays_list(self):
        """Test case for workdays_list

        List Workdays  # noqa: E501
        """
        pass

    def test_workdays_post(self):
        """Test case for workdays_post

        Create new Workday  # noqa: E501
        """
        pass

    def test_workdays_put(self):
        """Test case for workdays_put

        Update Workday  # noqa: E501
        """
        pass

    def test_workdays_settings(self):
        """Test case for workdays_settings

        Get Workday Settings (incomplete)  # noqa: E501
        """
        pass

    def test_workdays_workers(self):
        """Test case for workdays_workers

        List Workday Workers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
