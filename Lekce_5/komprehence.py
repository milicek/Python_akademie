word = "banana"
adjectives =["red", "big", "tasty"]
adjectives_plus_word = []

[adjectives_plus_word.append(adjective + " " + word) for adjective in adjectives]
print(adjectives_plus_word)

fib_numbers = [0, 1]
fib_number = 15

while len(fib_numbers) <=14:
    fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
print(fib_numbers)