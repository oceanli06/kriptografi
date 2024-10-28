import tkinter as tk
import pyperclip

def extended_vigenere_cipher(input_text, key):
    key_length = len(key)
    cipher_text = ""
    
    for i in range(len(input_text)):
        char = input_text[i]
        key_char = key[i % key_length]
        
        cipher_char = chr((ord(char) + ord(key_char)) % 256)
        cipher_text += cipher_char
    
    return cipher_text

def encrypt_text():
    input_text = entry_input_text.get()
    key = entry_key.get()
    cipher_text = extended_vigenere_cipher(input_text, key)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, cipher_text)

def decrypt_text():
    cipher_text = entry_cipher_text.get()
    key = entry_key.get()
    decrypted_text = ""
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key_char = key[i % len(key)]
        
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted_text += decrypted_char
    
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decrypted_text)

def copy_result():
    result_text = entry_result.get()
    pyperclip.copy(result_text)

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Extended Vigenere Cipher")

# Membuat label
label_input_text = tk.Label(root, text="Teks Input:")
label_key = tk.Label(root, text="Kunci:")
label_cipher_text = tk.Label(root, text="Teks Ciphertext:")
label_result = tk.Label(root, text="Hasil Enkripsi/Dekripsi:")

# Membuat entry (input) dan tombol
entry_input_text = tk.Entry(root)
entry_key = tk.Entry(root)
entry_cipher_text = tk.Entry(root)
entry_result = tk.Entry(root)
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_text)
decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt_text)
copy_button = tk.Button(root, text="Salin Hasil", command=copy_result)

# Menempatkan komponen-komponen ke dalam grid
label_input_text.grid(row=0, column=0)
label_key.grid(row=1, column=0)
label_cipher_text.grid(row=2, column=0)
label_result.grid(row=4, column=0, columnspan=2)

entry_input_text.grid(row=0, column=1)
entry_key.grid(row=1, column=1)
entry_cipher_text.grid(row=2, column=1)
entry_result.grid(row=5, column=0, columnspan=2)
encrypt_button.grid(row=3, column=0)
decrypt_button.grid(row=3, column=1)
copy_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
