
    # Чтение файла и подсчет частоты слов
word_freq = {}
with open('word_freq.txt', 'r') as file:
        for line in file:
            # line = line.strip()
            print(line)
            # freq, word = line.split()
            # word_freq[word] = int(freq)

    # Сортировка слов по частоте в убывающем порядке
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Вывод десяти самых популярных слов и их частот
for word, freq in sorted_words[:10]:
    print(f'Slovo: {word}, Chastota: {freq}')

