def isprime(x):
    if num > 1:
    # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

# Take inputs
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Ensure the numbers are in the right order
if lower > upper:
    lower, upper = upper, lower

# Loop
primes = []
for num in range(lower, upper + 1):
    if num % 2 == 1 and isprime(num):
        primes.append(num)

# Output
if len(primes) == 0:
    print("No prime numbers were found")
else:
    print(primes)
    