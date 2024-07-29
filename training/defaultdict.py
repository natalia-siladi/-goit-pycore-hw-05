from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
c = defaultdict(int)

# Збільшення значення для кожного ключа
c['a'] += 1
c['b'] += 1
c['a'] += 1

print(c)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)


grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))

