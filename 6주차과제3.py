from collections import Counter
def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()  
        words = text.split()
        return Counter(words)

file1_word_count = count_words_in_file('06 file01.txt')
file2_word_count = count_words_in_file('06 file02.txt')

common_words = file1_word_count.keys() & file2_word_count.keys()

print("공통된 단어와 각 파일에서의 빈도:")
for word in common_words:
    count1 = file1_word_count[word]
    count2 = file2_word_count[word]
    print(f"'{word}': 파일1 - {count1}, 파일2 - {count2}")
