import unittest
import subprocess
import io
import sys
from contextlib import redirect_stdout

class TestCountdownTimer(unittest.TestCase):

    def run_script_with_input(self, user_input):
        # Redirect stdout to capture print statements
        f = io.StringIO()
        with redirect_stdout(f):
            # Run the script with subprocess
            process = subprocess.Popen(['python3', 'countdown.py'], 
                                       stdin=subprocess.PIPE, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE)
            output, _ = process.communicate(input=user_input.encode())
        return output.decode()

    def test_valid_input(self):
        output = self.run_script_with_input('5\n')
        self.assertIn("Countdown is started.", output)
        self.assertIn("Remaining time: 00 : 00", output)
        self.assertIn("Countdown Finished...!", output)

    def test_zero_input(self):
        output = self.run_script_with_input('0\n')
        self.assertIn("Value must be posotive.", output)

    def test_negative_input(self):
        output = self.run_script_with_input('-5\n')
        self.assertIn("Value must be posotive.", output)

    def test_invalid_input(self):
        output = self.run_script_with_input('abc\n')
        self.assertIn("Invalid input..! Try to enter a valid input.", output)

    def test_large_input(self):
        # Test with a large input value
        output = self.run_script_with_input('3600\n')
        self.assertIn("Countdown is started.", output)
        self.assertIn("Remaining time: 59 : 59", output)

if __name__ == '__main__':
    unittest.main()
