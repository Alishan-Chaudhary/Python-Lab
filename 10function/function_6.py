def character(word):
    counts ={}
    for key in word:
        counts[key] = counts.get(key,0)+1
    return counts

n = input("Enter a word = ")
print(character(n))