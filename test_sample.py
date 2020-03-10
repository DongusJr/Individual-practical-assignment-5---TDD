from sample import fizz_buzz

# TODO: FIZZBUZZ:
#      1. Should return "Fizz" if number is divisable by 3
#      2. Should return "Buzz" if number is divisable by 5
#      3. Should return "FizzBuzz" if number is divisable by 3 and 5
#      4. Should return the number if none of the other requirements are met

def test_returns_number_if_no_requirements_met():
    assert fizz_buzz(2) == 2

def test_returns_Fizz_if_number_divisable_by_three():
    assert fizz_buzz(9) == "Fizz"