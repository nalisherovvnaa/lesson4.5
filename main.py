# masala 1
'''
def counter():
    count = 0

    def ichki():
        nonlocal count
        count += 1
        return count

    return ichki

counter_func = counter()

print(counter_func())
'''

#2
'''
def greater(chegara):
    def ichki(lst):
        result = []
        for x in lst:
            if x > chegara:
                result.append(x)
        return result
    return ichki

five = greater(5)
one = greater(1)

print(five([2, 4, 6, 1, 8]))
print(one([1, 0, 8]))
'''

# 3 masala
# 4 masala
'''
def tashqi(parity):
    def ichki(numbers):
        if parity == "even":
            return [num for num in numbers if num % 2 == 0]
        elif parity == "odd":
            return [num for num in numbers if num % 2 != 0]
        else:
            return "Error"
    return ichki

juft = tashqi("even")
toq = tashqi("odd")

print(juft([2, 3, 8]))
print(toq([2, 3, 8]))
'''

# 5 masala
'''
def filtr_palindromlar():
    def ichki(numbers):
        palindromes = []
        non_palindromes = []
        for num in numbers:
            if str(num) == str(num)[::-1]:
                palindromes.append(num)
            else:
                non_palindromes.append(num)
        return palindromes, non_palindromes
    return ichki

palindrome_func = filtr_palindromlar()

palindromes, non_palindromes = palindrome_func([121, 123, 12321, 567, 444])

print("Palindromlar:", palindromes)
print("Palindrom bolmaganlar:", non_palindromes)
'''

# 6 masala
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes():
    def inner(numbers):
        primes = []
        non_primes = []
        for num in numbers:
            if is_prime(num): 
                primes.append(num)
            else:
                non_primes.append(num)
        return primes, non_primes
    return inner

prime_func = filter_primes()

primes, non_primes = prime_func([2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Tub sonlar:", primes)
print("Murakkab sonlar:", non_primes)
'''