import sys
import unittest
from unittest.mock import patch


class TestVersion(unittest.TestCase):
    @patch("builtins.print")
    def test_version_argument(self, mock_print):
        test_args = ["uswfc", "--version"]
        with patch.object(sys, 'argv', test_args):
            from uswfc.cli import main
            with patch("uswfc.__version__", "1.0.0"):
                main()
                mock_print.assert_called_with("uswfc 1.0.0")