import inspect
import os
import sys


def import_tests():
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)


def test_logging_tools():
    import_tests()
    from pylogging_tools.tests import run_test
    assert run_test() is True
