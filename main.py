import hashlib
import os

def encrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    hashed_password = hashlib.sha256(password.encode()).digest()
    encrypted_content = hashed_password + file_content
    with open(file_path, 'wb') as file:
        file.write(encrypted_content)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        encrypted_content = file.read()
    hashed_password = hashlib.sha256(password.encode()).digest()
    if encrypted_content[:len(hashed_password)] == hashed_password:
        decrypted_content = encrypted_content[len(hashed_password):]
        with open(file_path, 'wb') as file:
            file.write(decrypted_content)
    else:
        print("Incorrect password for file:", file_path)

def encrypt_directory(directory_path, password):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            encrypt_file(file_path, password)

def decrypt_directory(directory_path, password):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            decrypt_file(file_path, password)
