# Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

# Perfect: aliquot sum = number
  # 6 is a perfect number because (1 + 2 + 3) = 6
  # 28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
  
# Abundant: aliquot sum > number
  # 12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
  # 24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36

# Deficient: aliquot sum < number
  # 8 is a deficient number because (1 + 2 + 4) = 7
  # Prime numbers are deficient
  
  def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
