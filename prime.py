def is_prime_num(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        limit = number**0.5 + 1
        i = 3
        while i <= limit:
            if number % i == 0:
                return False
            i += 2
        return True