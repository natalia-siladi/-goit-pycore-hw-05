import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

# Створення Counter з рядка
letter_count = collections.Counter("banana")
print(letter_count)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_count = collections.Counter(words)
print(word_count)
# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")