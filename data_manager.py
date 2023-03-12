import gspread
credentials = {

}
authorised_user = {

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







