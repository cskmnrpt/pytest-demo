import random

import pytest
from qase.pytest import qase


@qase.id(1)
def test_random_outcome():
    outcome = random.choice(["pass", "invalid"])

    if outcome == "pass":
        assert True  # Test passes
    elif outcome == "invalid":
        raise SyntaxError("Test resulted in an invalid state as per random choice")
