import pytest
import sys

sys.path.append("../src")

from disk import Disk

@pytest.fixture
def disk_test():
    return Disk(10)

def test_setSize_20(disk_test):
    disk_test.setSize(20)
    assert disk_test.getSize() == 20

def test_getSize(disk_test):
    disk_test.setSize(50)
    assert disk_test.getSize() == 50



