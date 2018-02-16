import unittest, os

def analyze_text(filename):
    """Calculates the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyse.

    Raises:
        IOError: If ''filename'' does not exist or cannot be read

    Returns:
        A tuple where the first element is the number of lines in
        the file and the second element is the number of characters.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)

class TextAnalysisTests(unittest.TestCase):
    """Tests the 'analyse_text function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Tiger Tiger burning bright\n'
                    'in the forests of the night.\n'
                    'What immortal hand or eye\n'
                    'could frame thy fearful symmetry')

    def tearDown(self):
        """Fixture that deletes the files used for testing."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run at all?"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 114)

    def test_no_such_file(self):
        """Check the proper error is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()
