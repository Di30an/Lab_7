import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimeSheet(TestCase):

    """ Mock input () to force it to return '2'"""
    # Patching the action of replacng a function or object with a mock
    @patch('builtins.input', side_effect= [2])
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2,hours)

    """ Verify the get_hours_for_day function ignres non-numnerica input"""
    # Side effect are a list of returns for your methods
    @patch('builtins.input', side_effect =['pizza', 'abc', '10abc', '2'])
    def test_get_hours_for_day_invaild(self, mock_input): # Mock input can be anything
        hours = timesheets.get_hours_for_day('whatever')
        self.assertEqual(2, hours)

    """ Verify the get_hours_for_day_validation"""
    # Tries all the options in the side_effect list and passes if any ONE of them are correct. 
    @ patch('builtins.input', side_effect =['cat', '123pizza', '2.4'])
    def test_get_hours_for_day_validation(self, mock_input):
        hours = timesheets.get_hours_for_day('whatever')
        self.assertEqual(2.4,hours)

    """ Mock the print function, check it was called with expected text"""
    @patch('builtins.print') # buitins.print. Differnet from buitins.inpt
    def test_display_print(self, mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_with('Total hours worked: 123')
    """ Mock the alert function so no actual beeping needed """
    # Patch is a function
    @patch('timesheets.alert')
    @patch('timesheets.print')
    # First argument is the innermost
    def test_alert_meet_min_hours_doesnt_meet(self, mock_print, mock_alert):
        timesheets.alert_not_meet_min_hours(10, 30)
        mock_alert.assert_called_once()
        mock_print.assert_called_once_with('You worked less than the minimum number of hours')


    @patch('timesheets.alert')
    @patch('timesheets.print')
    def test_alert_meet_min_hours_exceed(self, mock_alert, mock_print):
        timesheets.alert_not_meet_min_hours(45, 30)
        mock_alert.assert_not_called()
        mock_print.assert_not_called()
    @patch('builtins.print')
    def test_display_hours(self, mock_print):
        example = {'M':3 , 'T' : 12, 'W' : 8.5}

        expected_table_calls = [
            call('Day           Hours Worked    '),
            call('M             3               '),
            call('T             12              '),
            call('W             8.5             ')
        ]    
if __name__ == '__main__':
    unittest.main()