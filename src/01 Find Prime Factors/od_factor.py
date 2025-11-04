def find_prime_factors(n):
  prime_factors = []
  factor = 2
  for factor in range (2, n + 1):
    while n%factor == 0:
      n = n//factor
      prime_factors.append(factor)
    factor += 1
  return prime_factors

print(630, ":", find_prime_factors(630))  # [2, 3, 3, 5, 7]
print(13, ":", find_prime_factors(13))  # [13] 
print(84, ":", find_prime_factors(84))  # [2, 2, 3, 7]