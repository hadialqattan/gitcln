"""
CI integration tests for pycln module.
"""
from unittest import TestCase
from unittest.mock import patch
from argparse import Namespace
from os import mkdir, path

# local import
from gitcln.gitcln import main


class Gitcln_Integration_Tests(TestCase):
    """
    Integration tests for gitcln module.
    """

    def __init__(self, *args, **kwargs):
        super(Gitcln_Integration_Tests, self).__init__(*args, **kwargs)

    @classmethod
    def tearDownClass(cls):
        mkdir("tests/ignorefiles/__pycache__")
        for i in ["binary.so", "bytes.pyc", "file.log"]:
            with open("tests/ignorefiles/" + i, "w") as f:
                f.write("Created!")

    @patch("gitcln.gitcln.argsp")
    @patch("gitcln.gitcln.gitignore_reader")
    def test_01_remove_gitignore_files(self, gitignore_reader, argsp):
        """Test gitcln (ignorefiles)"""
        # patch CLI args
        argsp.return_value = Namespace(directories=[], files=[])
        # patch gitignore file
        gitignore_reader.return_value = (
            [],
            ["__pycache__"],
            ["*.py[cod]", "*.so", "*.log"],
        )
        # run main gitcln func
        main()
        # check
        assert path.exists("tests/ignorefiles/__pycache__") == False
        assert path.exists("tests/ignorefiles/binary.so") == False
        assert path.exists("tests/ignorefiles/bytes.pyc") == False
        assert path.exists("tests/ignorefiles/file.log") == False
