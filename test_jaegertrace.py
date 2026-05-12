# test_jaegertrace.py
"""
Tests for JaegerTrace module.
"""

import unittest
from jaegertrace import JaegerTrace

class TestJaegerTrace(unittest.TestCase):
    """Test cases for JaegerTrace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JaegerTrace()
        self.assertIsInstance(instance, JaegerTrace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JaegerTrace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
