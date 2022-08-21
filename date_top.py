from datetime import datetime

class Date:
    def __init__(self, given_date):
        self.given_date = given_date

    def year(self):
        return self.given_date.year

    def month(self):
        return self.given_date.month

    def odd_month(self):
        if self.given_date.month % 2 == 0:
            return True
        return False

    def current_year_is_leap_year(self):
        if self.given_date.year % 4 == 0:
            return True
        return False 

    def date_higher_than_today(self):
        dict_comparison = {}
        if self.given_date.day > datetime.now().day:
            dict_comparison["day"] = "Today is smaller than given today."
        else:
            dict_comparison["day"] = "Today is higher than given today."

        if self.given_date.month > datetime.now().month:
            dict_comparison["month"] = "Current month is smaller than given month."
        else:
            dict_comparison["month"] = "Current month is higher than given month."

        if self.given_date.year > datetime.now().year:
            dict_comparison["year"] = "Current year is smaller than given year."
        else:
            dict_comparison["year"] = "Current year is higher than given year."

        return dict_comparison

