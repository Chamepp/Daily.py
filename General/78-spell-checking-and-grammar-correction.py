from spellchecker import SpellChecker

def correct_text(text):
    spell = SpellChecker()
    # Split the text into individual words
    words = text.split()

    # Create a list to store corrected words
    corrected_words = []

    # Iterate over each word
    for word in words:
        # Check if the word is misspelled
        if word not in spell:
            # Get the most likely correct spelling
            corrected_word = spell.correction(word)
            # Append the corrected word to the list
            corrected_words.append(corrected_word)
        else:
            # Append the word as it is (already correct)
            corrected_words.append(word)

    # Join the corrected words back into a sentence
    corrected_text = ' '.join(corrected_words)
    return corrected_text

# Example usage
text = "Ths sentence has somee misspelled and grammatical errrors."
corrected_text = correct_text(text)
print("Original Text: ", text)
print("Corrected Text: ", corrected_text)
