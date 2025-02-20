word = "banana"
adjectives =["red", "big", "tasty"]
adjectives_plus_word = []

[adjectives_plus_word.append(adjective + " " + word) for adjective in adjectives]
print(adjectives_plus_word)