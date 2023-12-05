"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")
    else:
        list = [2]
        current_num = 2
        while len(list) < number_of_primes:
            is_primes = True
            for prime in list:
                if current_num % prime == 0:
                    is_primes = False
                    break

            if is_primes == True:
                list.append(current_num)

            current_num += 1

        return list

print(primes(20))