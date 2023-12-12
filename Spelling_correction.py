from textblob import TextBlob

def correct_spelling(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Correct spelling
    corrected_text = str(blob.correct())
    return corrected_text

def main():
    print("Welcome to Spelling Correction Tool!")
    text = input("Enter text with spelling mistakes: ")

    corrected_text = correct_spelling(text)
    print(f"Corrected text: {corrected_text}")

if __name__ == "__main__":
    main()
