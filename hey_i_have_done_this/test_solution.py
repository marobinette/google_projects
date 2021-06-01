import pytest
import hey_i_have_done_this.solution as sol

def test_sort_helper():
    assert sol.sort_helper(1211) == {
        "y": 1112,
        "x": 2111
    }


def test_get_diff():
    assert sol.get_diff(4, 999) == 0999