"""
Unit and regression test for the quickCSA package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import quickCSA


def test_quickCSA_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "quickCSA" in sys.modules
