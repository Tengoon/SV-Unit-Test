import unittest
import datetime
from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from TimeSeriesInput import TimeSeriesInput
from startDateInput import StartDateInput
from EndDateInput import EndDateInput
from Constants import Constants

class TestInputs(unittest.TestCase):

    def test_Symbols(self):
        s = SymbolInput()
        self.assertTrue(s.isInputValid('A'))
        self.assertTrue(s.isInputValid('AB'))
        self.assertTrue(s.isInputValid('ABC'))
        self.assertTrue(s.isInputValid('ABCD'))
        self.assertTrue(s.isInputValid('ABCDE'))
        self.assertFalse(s.isInputValid('ABCDEF'))
        self.assertFalse(sy.isInputValid('ABCDEFG'))
    
    def test_ChartType(self):
        chart = ChartTypeInput()
        self.assertTrue(chart.isInputValid("1"))
        self.assertTrue(chart.isInputValid("2"))
    
    def test_TimeSeries(self):
        ti = TimeSeriesInput()
        self.assertTrue(ti.isInputValid(1))
        self.assertTrue(ti.isInputValid(2))
        self.assertTrue(ti.isInputValid(3))
        self.assertTrue(ti.isInputValid(4))

    def test_startDate(self):
        sd = StartDateInput()
        self.assertTrue(sd.isInputValid("2020-03-01"))

    def test_endDate(self):
        ed = EndDateInput("2020-05-01")
        self.assertTrue(ed.isInputValid("2020-05-01"))

if __name__ == "__main__":
    unittest.main()
