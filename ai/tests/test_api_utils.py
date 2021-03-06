"""
Test the labAPi methods (api_utils.py)
"""

from ai.api_utils import LabApi
import sys
from unittest.mock import Mock, patch
from nose.tools import nottest, raises, assert_is_instance
import lab_api_mocker as mocker
import pandas as pd

class TestLabApi:
	def setup(self):
		"set up test fixtures"
		self.labApi = LabApi(
			api_path=mocker.api_path, 
			user=mocker.user, 
			api_key=None, 
			extra_payload=mocker.extra_payload,
			verbose=True)

	@patch('requests.request', side_effect=mocker.mocked_requests_request)
	def test_get_projects(self, mock_request):
		res = self.labApi.get_projects()
		#print("type: ", type(res))
		#assert_is_instance(res, dict)
		assert len(res) > 0


	@patch('requests.request', side_effect=mocker.mocked_requests_request)
	def test_get_all_ml_p(self, mock_request):
		res = self.labApi.get_all_ml_p()
		print("type: ", type(res))
		assert_is_instance(res, pd.DataFrame)
		assert len(res) > 0

	@patch('requests.request', side_effect=mocker.mocked_requests_request_multi_machine)
	def test_get_all_ml_p_mulit_machine(self, mock_request):
		res = self.labApi.get_all_ml_p()
		print("type: ", type(res))
		assert_is_instance(res, pd.DataFrame)
		assert len(res) > 0
		assert len(res) == 0