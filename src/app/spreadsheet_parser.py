from src.app.constants import ALL_GROUPS_SPREADSHEET_ID


class SpreadsheetParser():

    def __init__(self, google_api):
        self.google_api_service = google_api

    def get_all_groups(self):
        self.google_api_service.get_data(ALL_GROUPS_SPREADSHEET_ID)