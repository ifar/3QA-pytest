from operations import reciprocal, square, sqrt
import pytest


# reciprocal tests
def test_reciprocal_1():
    assert reciprocal(1) == 1


@pytest.mark.xfail(reason="Issue #1225: Reciprocal of zero is not handled")
def test_reciprocal_0():
    assert reciprocal(0) == "error"


def test_reciprocal_minus_2():
    assert reciprocal(-2) == -0.5


# sqrt tests
def test_sqrt_1():
    assert sqrt(1) == 1


def test_sqrt_4():
    assert sqrt(4) == 2


def test_sqrt_0():
    assert sqrt(0) == 0


@pytest.mark.xfail(reason="Issue #1224: Sqrt of zero is not handled",
                   strict=True)
def test_sqrt_minus_1():
    assert sqrt(-1) == "error"


# square test
def test_square_0():
    assert square(0) == 0


def test_square_1():
    assert square(1) == 1


def test_square_2():
    assert square(2) == 4


def test_square_minus_1():
    assert square(-1) == 1
