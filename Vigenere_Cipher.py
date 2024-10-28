from tkinter import *

def vigenere_cipher(text, key, mode):
    # Convert text and key to uppercase
    text = text.upper()
    key = key.upper()

    # Generate key of the same length as text
    key = key * (len(text) // len(key) + 1)
    key = key[:len(text)]

    # Encrypt or decrypt text using Vigenere Cipher
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if mode == "encrypt":
                result += chr((ord(text[i]) + ord(key[i])) % 26 + ord('A'))
            elif mode == "decrypt":
                result += chr((ord(text[i]) - ord(key[i])) % 26 + ord('A'))
        else:
            result += text[i]

    return result

def encrypt():
    # Get input from user
    text = text_input.get("1.0", END).strip()
    key = key_input.get().strip()

    # Encrypt text using Vigenere Cipher
    result = vigenere_cipher(text, key, "encrypt")

    # Display result
    result_output.delete("1.0", END)
    result_output.insert(END, result)

def decrypt():
    # Get input from user
    text = text_input.get("1.0", END).strip()
    key = key_input.get().strip()

    # Decrypt text using Vigenere Cipher
    result = vigenere_cipher(text, key, "decrypt")

    # Display result
    result_output.delete("1.0", END)
    result_output.insert(END, result)

# Create GUI
root = Tk()
root.title("Vigenere Cipher")

# Create input widgets
text_label = Label(root, text="Text:")
text_input = Text(root, height=5, width=50)
key_label = Label(root, text="Key:")
key_input = Entry(root)
encrypt_button = Button(root, text="Encrypt", command=encrypt)
decrypt_button = Button(root, text="Decrypt", command=decrypt)

# Create output widget
result_output = Text(root, height=5, width=50)

# Pack widgets
text_label.pack()
text_input.pack()
key_label.pack()
key_input.pack()
encrypt_button.pack()
decrypt_button.pack()
result_output.pack()

# Start GUI
root.mainloop()