from sample import fizz_buzz

def test_returns_number_if_no_requirements_met():
    assert fizz_buzz(2) == 2

def test_returns_Fizz_if_number_divisable_by_three():
    assert fizz_buzz(9) == "Fizz"

def test_returns_Buzz_if_number_divisable_by_five():
    assert fizz_buzz(10) == "Buzz"

def test_returns_FizzBuzz_if_number_divisable_by_three_and_five():
    assert fizz_buzz(15) == "FizzBuzz"