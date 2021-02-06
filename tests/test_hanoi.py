import pytest
import sys
sys.path.append("../src")

from hanoi import Hanoi

@pytest.fixture
def sample_hanoi():
    h = Hanoi()
    return h

def test_move_invalid_source(sample_hanoi):
    with pytest.raises(ValueError, match=r'Source.*is invalid'):
        sample_hanoi.move(-1, 2)

def test_move_invalid_source2(sample_hanoi):
    with pytest.raises(ValueError, match=r'Source.*is invalid'):
        sample_hanoi.move(10, 2)

def test_move_invalid_target(sample_hanoi):
    with pytest.raises(ValueError, match=r'Target.*is invalid'):
        sample_hanoi.move(0, -3)

def test_move_invalid_target2(sample_hanoi):
    with pytest.raises(ValueError, match=r'Target.*is invalid'):
        sample_hanoi.move(0, 15)

def test_move_invalid_source_target_same(sample_hanoi):
    with pytest.raises(Exception, match=r'Source\s+and\s+Target.*cannot be equal'):
        sample_hanoi.move(1, 1)

def test_move_invalid_empty_source_disk(sample_hanoi):
    with pytest.raises(Exception, match=r'Source.*nothing\s+to\s+move'):
        sample_hanoi.move(2, 1)

def test_move_invalid_big_on_small(sample_hanoi):
    sample_hanoi.move(0, 1)
    with pytest.raises(Exception, match=r'Source.*is bigger.*Target'):
        sample_hanoi.move(0, 1)

def test_state_valid_move(sample_hanoi):
    sample_hanoi.move(0, 1)
    assert sample_hanoi.getState()
    assert sample_hanoi.rob1.getAllDisks() == [1]

def test_state_valid_multiple_move(sample_hanoi):
    sample_hanoi.move(0, 1)
    sample_hanoi.move(0, 2)
    sample_hanoi.move(1, 2)
    sample_hanoi.move(0, 1)
    sample_hanoi.move(2, 0)
    assert sample_hanoi.rob0.getAllDisks() == [4, 1]
    assert sample_hanoi.rob1.getAllDisks() == [3]
    assert sample_hanoi.rob2.getAllDisks() == [2]

def test_initial_not_win(sample_hanoi):
    assert sample_hanoi.isWin() == False

def test_in_progress_not_win(sample_hanoi):
    sample_hanoi.move(0, 1)
    sample_hanoi.move(0, 2)
    sample_hanoi.move(1, 2)
    sample_hanoi.move(0, 1)
    sample_hanoi.move(2, 0)
    sample_hanoi.move(2, 1)
    sample_hanoi.move(0, 1)
    sample_hanoi.move(0, 2)
    assert sample_hanoi.isWin() == False

def test_win(sample_hanoi):
    sample_hanoi.move(0, 1)
    sample_hanoi.move(0, 2)
    sample_hanoi.move(1, 2)
    sample_hanoi.move(0, 1)
    sample_hanoi.move(2, 0)
    sample_hanoi.move(2, 1)
    sample_hanoi.move(0, 1)
    sample_hanoi.move(0, 2)
    sample_hanoi.move(1, 2)
    sample_hanoi.move(1, 0)
    sample_hanoi.move(2, 0)
    sample_hanoi.move(1, 2)
    sample_hanoi.move(0, 1)
    sample_hanoi.move(0, 2)
    sample_hanoi.move(1, 2)
    assert sample_hanoi.rob2.getAllDisks() == [4 ,3 ,2, 1]
    assert sample_hanoi.rob0.getAllDisks() == []
    assert sample_hanoi.isWin() == True