import unittest
from freezegun import freeze_time
from datetime import datetime
from date_top import Date

class TestDate(unittest.TestCase):

    def setUp(self):
        self.current_date = datetime.now()

    # def test_odd_month(self):
    #     """Must return True"""
    #     date_obj = Date(given_date=self.current_date)
    #     self.assertEqual(date_obj.odd_month(), True)

    # def test_even_month(self):
    #     date_obj = Date(given_date=self.current_date)
    #     """Must return False"""
    #     self.assertEqual(date_obj.odd_month(), False)

    @freeze_time("2012-02-14")
    def test_odd_month_freezegun(self):
        """Must return True"""
        date_obj = Date(given_date=datetime.now())
        self.assertEqual(date_obj.odd_month(), True)
    
    @freeze_time("2012-01-14")
    def test_even_month_freezegun(self):
        """Must return False"""
        date_obj = Date(given_date=datetime.now())
        self.assertEqual(date_obj.odd_month(), False)

    @freeze_time("2022-9-21")
    def test_comparation_today_with_yesterday_day(self):
        yesterday = datetime(2022, 9, 20)
        date_obj = Date(given_date=yesterday)
        self.assertEqual(date_obj.date_higher_than_today()["day"], "Today is higher than given today.")

    @freeze_time("2022-9-21")
    def test_comparation_today_with_yesterday_month(self):
        yesterday = datetime(2022, 9, 20)
        date_obj = Date(given_date=yesterday)
        self.assertEqual(date_obj.date_higher_than_today()["month"], "Current month is higher than given month.")

    @freeze_time("2022-9-21")
    def test_comparation_today_with_yesterday_year(self):
        yesterday = datetime(2022, 9, 20)
        date_obj = Date(given_date=yesterday)
        self.assertEqual(date_obj.date_higher_than_today()["year"], "Current year is higher than given year.")

if __name__ == "__main__":
    unittest.main()