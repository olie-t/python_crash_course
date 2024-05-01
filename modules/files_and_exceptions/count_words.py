from pathlib import Path


def count_words(file_path):
    contents = Path(file_path)
    raw_text = contents.read_text()
    words = {}
    for word in raw_text.split():
        if word.lower() not in words:
            words[word.lower()] = 1
        else:
            words[word.lower()] += 1
    print(words)

if __name__ == "__main__":
    count_words('illiad.txt')
    count_words('the_importance_of_being_earnest.txt')
