# prime numbers

def is_prime(number):

    if number <= 1:
        return False
    else:
        for i in range (2, number):
            if number % i == 0:
                return False
        return True

prime_num_list = [i for i in range (2, 50)
                  if is_prime(i)]
print(prime_num_list)