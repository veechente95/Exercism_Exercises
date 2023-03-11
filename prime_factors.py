def factors(start_num):
    prime_factors = []
    factor = 2                  # Begin with a Divisor of 2
    while start_num > 1:
        if start_num % factor == 0:
            prime_factors.append(factor)
            start_num /= factor  # divide the num by the factor 
        else: 
            factor += 1         # If the divisor is not a factor increase it by 1
    return prime_factors
