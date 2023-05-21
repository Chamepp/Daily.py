import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def paste_from_clipboard():
    return pyperclip.paste()

# Example usage:
text_to_copy = "Hello, world!"
copy_to_clipboard(text_to_copy)

# Now the text "Hello, world!" is copied to the clipboard
# Let's paste it and print the result:
pasted_text = paste_from_clipboard()
print("Pasted text:", pasted_text)
