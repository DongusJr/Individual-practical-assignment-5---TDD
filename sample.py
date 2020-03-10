def fizz_buzz(number):
    fizz_buzz_str = ""
    if number % 3 == 0:
        fizz_buzz_str += "Fizz"
    return fizz_buzz_str if fizz_buzz_str != "" else number