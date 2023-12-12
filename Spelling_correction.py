from textblob import TextBlob

words = []  # List to store words

def correct_spelling(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Correct spelling
    corrected_text = str(blob.correct())
    return corrected_text

def add_word():
    word = input("Enter a word with spelling mistakes: ")
    corrected_word = correct_spelling(word)
    words.append(corrected_word)
    print(f"'{word}' has been added and corrected to '{corrected_word}'.")

def view_words():
    if len(words) == 0:
        print("No words added yet.")
    else:
        print("List of words:")
        for idx, word in enumerate(words, start=1):
            print(f"{idx}. {word}")

def main():
    print("Welcome to Spelling Correction Tool!")
    while True:
        print("\nMENU:")
        print("1. Write a word")
        print("2. View your words")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_word()
        elif choice == '2':
            view_words()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
