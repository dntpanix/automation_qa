import unittest
from unittest.mock import patch, Mock
from mock_api import APIClient

class TestAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_ok(self, mock_get):
        preset_data = {"status":"ok"}
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = preset_data
        mock_get.return_value = mock_response

        base_url="https://localhost.com"

        # test
        api_client = APIClient(base_url)
        result = api_client.get_data()

        mock_get.assert_called_once_with(f"{base_url}/data")

        self.assertEqual(result, preset_data)

    # def test_real_get_data_ok(self):
    #     preset_data = {"status":"ok"}
    #     base_url="https://localhost.com"

    #     # test
    #     api_client = APIClient(base_url)
    #     result = api_client.get_data()

    #     self.assertEqual(result, preset_data)

if __name__ == '__main__':
    unittest.main()