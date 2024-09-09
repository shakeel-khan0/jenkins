import unittest
from io import StringIO
import sys
import time

class TestCountdown(unittest.TestCase):
    def test_valid_input(self):
        # Capture the output
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # Simulate user input
        sys.stdin = StringIO('5\n')
        
        # Run the script
        exec(open('countdown.py').read())
        
        # Check output
        output = sys.stdout.getvalue()
        self.assertIn("Countdown Finished", output)
        
        sys.stdout = old_stdout

    def test_invalid_input(self):
        # Simulate invalid input
        sys.stdin = StringIO('invalid\n')
        
        # Run the script
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        exec(open('countdown.py').read())
        output = sys.stdout.getvalue()
        self.assertIn("Invalid input", output)
        
        sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main()
