import random

PRIME = 2087

def gencoeff(secret, k):
    coeffs = [secret]
    for i in range(k - 1):
        coeffs.append(random.randint(0, PRIME))
    return coeffs

def evalpoly(coeffs, x):
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] * (x ** i)
    return result % PRIME

def genshares(secret, n, k):
    coeffs = gencoeff(secret, k)
    shares = []
    for x in range(1, n + 1):
        y = evalpoly(coeffs, x)
        shares.append((x, y))
    return shares

def lagrange_interpolation(x, x_s, y_s):
    total = 0
    k = len(x_s)
    for i in range(k):
        xi = x_s[i]
        yi = y_s[i]
        prod = 1
        for j in range(k):
            if i != j:
                xj = x_s[j]
                prod *= (x - xj) * pow(xi - xj, -1, PRIME)
                prod %= PRIME
        total += yi * prod
        total %= PRIME
    return total

secret = 1234
n = 5
k = 3

shares = genshares(secret, n, k)
print("Generated Shares:")
for s in shares:
    print(s)

sample = shares[:k]
x_s = [s[0] for s in sample]
y_s = [s[1] for s in sample]

recovered = lagrange_interpolation(0, x_s, y_s)
print("\nRecovered Secret:", recovered)