import random
from matplotlib import pyplot as plt

prime = 2017
secret = int(input("What is the secret?:"))
shares_no = int(input("how many shares do you want?:"))
threshold = int(input("what is the threshold number of shares?:"))

coefficients = random.sample(range(1,prime), k=threshold-1)
coefficients.insert(0,secret)
x_values = random.sample(range(1,prime), k=shares_no)

def fx_calc(x_values,coefficients):
    def f(x):
        fx = 0
        for ind,i in enumerate(coefficients):
            fx+=i*(x**ind)
        return fx

    fx_values = []
    for x in x_values:
        fx = f(x)%prime
        fx_values.append(fx)
    return fx_values

fx_values = fx_calc(x_values,coefficients)

coords = list(zip(x_values,fx_values))
#coords = random.sample(coords,threshold)
print("coordinates",coords,"coefficients",coefficients,sep="\n")

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def lagrange(points):
    def P(x):
        total = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]

            def g(i, n):

                tot_mul = 1
                for j in range(n):
                    if i == j:
                        continue
                    xj, yj = points[j]
                    #tot_mul *= (x - xj) / float(xi - xj)
                    numerator = (x - xj)%prime
                    denominator =(xi - xj)%prime

                    tot_mul *= numerator*modinv(denominator, prime)%prime

                return tot_mul%prime

            total += (yi * g(i, n))%prime
        return total%prime
    return P

print("recovered password:", lagrange(coords)(0))
