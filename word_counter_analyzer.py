# Word Count and Text Analyzer

def analyze_text(text):
    words = text.split()

    word_count = len(words)
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    print("\n----- Analysis Result -----")
    print("Total Words:", word_count)
    print("Total Characters:", char_count)
    print("Total Sentences:", sentence_count)

    # Frequency of words
    frequency = {}

    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(word, ":", count)

# Main Program
try:
    text = input("Enter a paragraph:\n")

    if not text.strip():
        raise ValueError("Text cannot be empty.")

    analyze_text(text)

except ValueError as e:
    print("Error:", e)