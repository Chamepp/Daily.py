from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def main():
    # Prompt the user for input
    text = input("Enter the text you want to translate: ")
    source_lang = input("Enter the source language code (e.g., 'en' for English): ")
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ")

    # Call the translation function
    translated_text = translate_text(text, source_lang, target_lang)

    # Print the translated text
    print("Translated Text:")
    print(translated_text)

if __name__ == '__main__':
    main()
