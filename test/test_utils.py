import unittest, sys, tempfile
from parameterized import parameterized_class
from src.utils import Utils

class TestUtils(unittest.TestCase):
  def test_split(self):
    assert (not Utils.split([]))
    assert (Utils.split(["a", "b", "c", "d"]) == (["a", "b", "c", "d"], None))
    with tempfile.TemporaryDirectory() as tmpdirname:
      assert (Utils.split(["a", "b", "c", tmpdirname]) == (["a", "b", "c"], tmpdirname))
