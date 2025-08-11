
with open("python.txt",'r') as file:
    text = file.read()

words = text.split()

word_counts = {}
for word in words:
    if word:
        word_counts[word] = word_counts.get(word,0)+1

most_common = max(word_counts, key = word_counts.get)
print(most_common,word_counts[most_common])
print(word,word_counts[word])