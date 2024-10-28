import random
import tkinter as tk

# Fungsi untuk mengenkripsi pesan dengan OTP
def encrypt_message():
    plaintext = input_text.get().upper()
    key = generate_random_key(len(plaintext))
    
    encrypted_text = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            encrypted_char = encrypt_char(char, key[i])
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    output_text.set(encrypted_text)
    key_text.set("Kunci: " + "".join(key))

# Fungsi untuk mendekripsi pesan dengan OTP
def decrypt_message():
    encrypted_text = input_text.get().upper()
    key = key_text.get()[7:]  # Mengambil kunci dari label (menghilangkan "Kunci: ")
    
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            decrypted_char = decrypt_char(char, key[i])
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    output_text.set(decrypted_text)

# Fungsi untuk mengenkripsi satu karakter dengan OTP
def encrypt_char(char, key_char):
    char_index = ord(char) - ord('A')
    key_index = ord(key_char) - ord('A')
    encrypted_index = (char_index + key_index) % 26
    return chr(encrypted_index + ord('A'))

# Fungsi untuk mendekripsi satu karakter dengan OTP
def decrypt_char(char, key_char):
    char_index = ord(char) - ord('A')
    key_index = ord(key_char) - ord('A')
    decrypted_index = (char_index - key_index) % 26
    return chr(decrypted_index + ord('A'))

# Fungsi untuk menghasilkan kunci acak dengan panjang tertentu
def generate_random_key(length):
    return [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length)]

# Membuat jendela tkinter
window = tk.Tk()
window.title("One-time Pad (OTP) Cipher")
window.geometry("400x250")

# Label dan input teks
tk.Label(window, text="Masukkan pesan:").pack()
input_text = tk.StringVar()
input_entry = tk.Entry(window, textvariable=input_text)
input_entry.pack()

# Tombol untuk mengenkripsi
encrypt_button = tk.Button(window, text="Enkripsi", command=encrypt_message)
encrypt_button.pack()

# Tombol untuk mendekripsi
decrypt_button = tk.Button(window, text="Dekripsi", command=decrypt_message)
decrypt_button.pack()

# Hasil enkripsi atau dekripsi
output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text)
output_label.pack()

# Label untuk kunci
key_text = tk.StringVar()
key_label = tk.Label(window, textvariable=key_text)
key_label.pack()

# Memulai jendela GUI
window.mainloop()