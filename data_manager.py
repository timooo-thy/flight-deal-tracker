import gspread
credentials = {
    "installed": {
        "client_id": "652023713794-kmnuveuoq8agppe5umfvt9jckqj751bg.apps.googleusercontent.com",
        "project_id": "flight-club-355508",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": ["http://localhost"]
    }
}
authorised_user = {
    "refresh_token": "1//0govFtBt6w3muCgYIARAAGBASNwF-L9Ira0IWQBBLKZumo9fOMUGeuxgw5WjSKisU0-WtkLnlC_0m4Z567F5Eh1Ou-Bd24RQxytc",
    "token_uri": "https://oauth2.googleapis.com/token",
    "client_id": "652023713794-kmnuveuoq8agppe5umfvt9jckqj751bg.apps.googleusercontent.com",
    "client_secret": "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",
    "scopes": ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"],
    "expiry": "2022-07-06T11:50:03.496209Z"
}
gc, authorised_user = gspread.oauth_from_dict(credentials, authorised_user)
sh = gc.open("Flight Deals")

class DataManager:

    def __init__(self):
        self.city = []
        self.price = []
        self.email = []

    def get_data(self):
        prices_sheet = sh.worksheet("prices")
        self.city = prices_sheet.col_values(1)[1:]
        self.price = prices_sheet.col_values(3)[1:]

    def edit_row(self, code, row, column):
        prices_sheet = sh.worksheet("prices")
        prices_sheet.update_cell(row, column, code)

    def get_customer_emails(self):
        user_sheet = sh.worksheet("users")
        self.email = user_sheet.col_values(3)[1:]
        return self.email







