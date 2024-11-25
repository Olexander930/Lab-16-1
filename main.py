import nltk
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg

# Завантаження необхідних ресурсів
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

# Завантажуємо текст із архіву Project Gutenberg
text = gutenberg.raw('chesterton-ball.txt')  

# Визначення кількості слів у тексті
def count_words(text):
    words = nltk.word_tokenize(text)
    return len(words)

# Визначення 10 найбільш вживаних слів
def most_used_words(words, title, color):
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(10)

    # Побудова графіка
    words_list = [word for word, count in most_common_words]
    counts_list = [count for word, count in most_common_words]

    plt.figure(figsize=(10, 6))
    plt.bar(words_list, counts_list, color=color)
    plt.title(title)
    plt.xlabel('Слова')
    plt.ylabel('Кількість повторень')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return most_common_words

# Видалення пунктуації та стоп-слів
def clean_text(words):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    cleaned_words = [
        word.lower() for word in words
        if word.lower() not in stop_words and
        word not in string.punctuation
    ]
    return cleaned_words

# Основна частина
print("Аналіз тексту з Project Gutenberg:")
total_words = nltk.word_tokenize(text)
word_count = count_words(text)
print(f"Кількість слів у тексті: {word_count}")

# Аналіз без очищення тексту
print("\n10 найбільш вживаних слів (до очищення):")
raw_most_common = most_used_words(total_words, "10 найбільш вживаних слів (до очищення)", "red")
for word, count in raw_most_common:
    print(f"{word}: {count}")

# Очищення тексту
cleaned_words = clean_text(total_words)
cleaned_word_count = len(cleaned_words)
print(f"\nКількість слів після очищення: {cleaned_word_count}")

# Аналіз після очищення тексту
print("\n10 найбільш вживаних слів (після очищення):")
cleaned_most_common = most_used_words(cleaned_words, "10 найбільш вживаних слів (після очищення)", "green")
for word, count in cleaned_most_common:
    print(f"{word}: {count}")

