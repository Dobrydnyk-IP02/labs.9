import test_1

str=test_1.user_input()
test_1.output()
words=str.split()
number_words=len(words)
print("number of words: ", number_words)

min_index=test_1.search_min(number_words, words)
min = words[min_index]
print("min: ", words[min_index])

max_index=test_1.search_max(number_words, words)
max = words[max_index]
print("max: ", words[max_index])

words[min_index] = max
words[max_index] = min

print("str: ", words)