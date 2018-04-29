from mock import Mock
from src.app.spreadsheet_parser import SpreadsheetParser
from src.app.constants import ALL_GROUPS_SPREADSHEET_ID


def test_should_get_data_from_google_api_from_all_groups_file():
    mock_google_api = Mock()
    spreadsheet_parser = SpreadsheetParser(mock_google_api)
    spreadsheet_parser.get_all_groups()

    mock_google_api.get_data.assert_called_with(ALL_GROUPS_SPREADSHEET_ID)