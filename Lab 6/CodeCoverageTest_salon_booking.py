import pytest
from salon_booking import extra_time_charge, can_book, arrival_status

# Example test cases:
def test_within_included_time():
    assert extra_time_charge("haircut", 20, "junior", False) == 0

def test_can_book():
    assert can_book(2, 1, False) is True

# Step 5: Test cases for >90% code (line) coverage
def test_extra_time_junior_member():
    assert extra_time_charge("haircut", 50, "junior", True) == 50

def test_extra_time_senior_over_60():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100

def test_can_book_walk_in_and_large_party():
    assert can_book(2, 1, True) is True
    assert can_book(5, 1, False) is False

def test_arrival_status_cases():
    assert arrival_status(25, True, True) == "open"
    assert arrival_status(5, False, True) == "late"
    assert arrival_status(-5, False, True) == "closed"

