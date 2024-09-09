import unittest
import subprocess
import io
from contextlib import redirect_stdout

class TestCountdownTimer(unittest.TestCase):

    def run_script(self):
        # Redirect stdout to capture print statements
        f = io.StringIO()
        with redirect_stdout(f):
            # Run the script with subprocess
            process = subprocess.Popen(['python3', 'countdown.py'], 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE)
            output, _ = process.communicate()
        return output.decode()

    def test_default_value(self):
        output = self.run_script()
        self.assertIn("Countdown is started.", output)
        self.assertIn("Remaining time: 00 : 00", output)
        self.assertIn("Countdown Finished...!", output)

if __name__ == '__main__':
    unittest.main()
