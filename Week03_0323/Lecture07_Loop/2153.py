import math

def converter(w):
    if(w.isupper()):
        return ord(w) - 38
    return ord(w) - 96
def isPrime(n):
    if n < 1:
        return "It is not a prime word."
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return "It is not a prime word."
    return "It is a prime word."

w = input()
word_sum = 0
for i in w:
    word_sum += converter(i)
print(isPrime(word_sum))
