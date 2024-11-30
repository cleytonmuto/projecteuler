from math import sqrt

def count_divisors(n):
  array = []
  for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
      array.append(i)
      if i != n // i:
        array.append(n // i)
  return len(array)

def triangle_number(n) -> int:
   return int(n * (n + 1) / 2)

def main():
    n = 1
    while count_divisors(triangle_number(n)) < 500:
       n += 1
    print(triangle_number(n))
        
if __name__ == "__main__":
    main()