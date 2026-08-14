# test_pivotgate.py
"""
Tests for PivotGate module.
"""

import unittest
from pivotgate import PivotGate

class TestPivotGate(unittest.TestCase):
    """Test cases for PivotGate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PivotGate()
        self.assertIsInstance(instance, PivotGate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PivotGate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
