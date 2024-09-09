import unittest
from unittest.mock import patch
from your_script import countdown  # Replace 'your_script' with the actual script name

class TestCountdown(unittest.TestCase):

    @patch('builtins.print')
    @patch('time.sleep', return_value=None)  # Mock time.sleep to speed up the test
    def test_countdown_default_value(self, mock_sleep, mock_print):
        countdown()  # Using the default value of 10 seconds

        # Check that the countdown started message is printed
        mock_print.assert_any_call('Countdown is started.')

        # Verify that countdown messages from 10 to 0 are printed correctly
        for i in range(10, -1, -1):
            minutes = i // 60
            seconds = i % 60
            mock_print.assert_any_call(f'Remaining time: {minutes:02d} : {seconds:02d}', end='\r')

        # Check that the countdown finished message is printed
        mock_print.assert_any_call('Countdown Finished!...!')

if __name__ == '__main__':
    unittest.main()
