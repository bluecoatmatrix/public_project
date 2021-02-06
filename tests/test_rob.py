import pytest
import sys
sys.path.append("../src")
from rob import Rob
from disk import Disk

def test_push_disk():
    r = Rob()
    d = Disk(10)
    r.pushDisk(d)
    assert r.getNumDisks() == 1
    assert r.peekDisk().getSize() == 10

def test_pop_disk_valid():
    r = Rob()
    d1 = Disk(1)
    d2 = Disk(2)
    r.pushDisk(d1)
    r.pushDisk(d2)
    d_pop = r.popDisk()
    assert d_pop.getSize() == 2
    assert r.getNumDisks() == 1
    assert r.peekDisk().getSize() == 1

def test_pop_empty_exception():
    r = Rob()
    with pytest.raises(Exception, match=r'.*nothing to pop'):
        r.popDisk()

def test_peek_disk_valid():
    r = Rob()
    d1 = Disk(5)
    r.pushDisk(d1)
    d_peek = r.peekDisk()
    assert d_peek.getSize() == 5
    assert r.getNumDisks() == 1

def test_peek_empty_exception():
    r = Rob()
    with pytest.raises(Exception, match=r'.*nothing to peek'):
        r.peekDisk()

def test_get_number_disk():
    r = Rob()
    d1 = Disk(1)
    d2 = Disk(2)
    r.pushDisk(d1)
    r.pushDisk(d2)
    assert r.getNumDisks() == 2
    r.popDisk()
    assert r.getNumDisks() == 1
    r.popDisk()
    assert r.getNumDisks() == 0

def test_get_All_disks():
    r = Rob()
    d1 = Disk(37)
    d2 = Disk(25)
    d3 = Disk(12)
    r.pushDisk(d1)
    r.pushDisk(d2)
    r.pushDisk(d3)
    assert r.getAllDisks() == [37, 25, 12]
