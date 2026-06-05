import pytest

from calculator import add, divide, multiply, subtract


class TestAdd:
    def test_positive_numbers(self) -> None:
        assert add(2, 3) == 5

    def test_negative_numbers(self) -> None:
        assert add(-1, -1) == -2

    def test_mixed_sign(self) -> None:
        assert add(-1, 1) == 0

    def test_zeros(self) -> None:
        assert add(0, 0) == 0

    def test_floats(self) -> None:
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    def test_positive_result(self) -> None:
        assert subtract(5, 3) == 2

    def test_negative_result(self) -> None:
        assert subtract(0, 5) == -5

    def test_same_numbers(self) -> None:
        assert subtract(7, 7) == 0


class TestMultiply:
    def test_positive_numbers(self) -> None:
        assert multiply(3, 4) == 12

    def test_negative_numbers(self) -> None:
        assert multiply(-2, 3) == -6

    def test_by_zero(self) -> None:
        assert multiply(0, 100) == 0

    def test_floats(self) -> None:
        assert multiply(2.5, 4.0) == 10.0


class TestDivide:
    def test_exact_division(self) -> None:
        assert divide(10, 2) == 5.0

    def test_float_result(self) -> None:
        assert divide(7, 2) == 3.5

    def test_negative_divisor(self) -> None:
        assert divide(-10, 2) == -5.0

    def test_divide_by_zero_raises(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
