import tkinter as tk

def prepare_key(key):
    key = key.replace('J', 'I')
    key = ''.join(dict.fromkeys(key))
    key = key.replace(' ', '').upper()
    
    # Membuat matriks kunci
    key_matrix = [[0] * 5 for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    key = key + alphabet
    
    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = key[i * 5 + j]
    
    return key_matrix

def playfair_encrypt(plain_text, key_matrix):
    plain_text = plain_text.replace('J', 'I')
    plain_text = plain_text.replace(' ', '').upper()
    
    encrypted_text = ''
    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        i += 1
        
        if i == len(plain_text):
            char2 = 'X'
        else:
            char2 = plain_text[i]
            if char2 == char1:
                char2 = 'X'
                i -= 1
        
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        
        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5]
            encrypted_text += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1]
            encrypted_text += key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2]
            encrypted_text += key_matrix[row2][col1]
        
        i += 1
    
    return encrypted_text

def playfair_decrypt(encrypted_text, key_matrix):
    decrypted_text = ''
    i = 0
    while i < len(encrypted_text):
        char1 = encrypted_text[i]
        i += 1
        
        if i == len(encrypted_text):
            char2 = 'X'
        else:
            char2 = encrypted_text[i]
        
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        
        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5]
            decrypted_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1]
            decrypted_text += key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]
        
        i += 1
    
    return decrypted_text

def find_char_position(key_matrix, char):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j
    return -1, -1

def encrypt_text():
    plain_text = entry_plain_text.get()
    key = entry_key.get()
    key_matrix = prepare_key(key)
    encrypted_text = playfair_encrypt(plain_text, key_matrix)
    entry_encrypted_text.delete(0, tk.END)
    entry_encrypted_text.insert(0, encrypted_text)

def decrypt_text():
    encrypted_text = entry_encrypted_text.get()
    key = entry_key.get()
    key_matrix = prepare_key(key)
    decrypted_text = playfair_decrypt(encrypted_text, key_matrix)
    entry_plain_text.delete(0, tk.END)
    entry_plain_text.insert(0, decrypted_text)

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Playfair Cipher")

# Membuat label
label_plain_text = tk.Label(root, text="Plaintext:")
label_key = tk.Label(root, text="Kunci:")
label_encrypted_text = tk.Label(root, text="Ciphertext:")

# Membuat entry (input) dan tombol
entry_plain_text = tk.Entry(root)
entry_key = tk.Entry(root)
entry_encrypted_text = tk.Entry(root)
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_text)
decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt_text)

# Menempatkan komponen-komponen ke dalam grid
label_plain_text.grid(row=0, column=0)
label_key.grid(row=1, column=0)
label_encrypted_text.grid(row=2, column=0)

entry_plain_text.grid(row=0, column=1)
entry_key.grid(row=1, column=1)
entry_encrypted_text.grid(row=2, column=1)
encrypt_button.grid(row=3, column=0)
decrypt_button.grid(row=3, column=1)

root.mainloop()
