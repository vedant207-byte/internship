def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def multi_encrypt(text, caesar_shift, vigenere_key):
    caesar_encrypted = caesar_encrypt(text, caesar_shift)
    return vigenere_encrypt(caesar_encrypted, vigenere_key)

def multi_decrypt(text, caesar_shift, vigenere_key):
    vigenere_decrypted = vigenere_decrypt(text, vigenere_key)
    return caesar_decrypt(vigenere_decrypted, caesar_shift)

def main():
    print("Custom Encryption-Decryption System")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Multi-layer (Caesar + Vigenère)")

    choice = input("Choose encryption method (1/2/3): ")

    if choice == "1":
        text = input("Enter your message: ")
        shift = int(input("Enter Caesar shift value: "))
        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
    elif choice == "2":
        text = input("Enter your message: ")
        key = input("Enter Vigenère key: ")
        encrypted = vigenere_encrypt(text, key)
        decrypted = vigenere_decrypt(encrypted, key)
    elif choice == "3":
        text = input("Enter your message: ")
        shift = int(input("Enter Caesar shift value: "))
        key = input("Enter Vigenère key: ")
        encrypted = multi_encrypt(text, shift, key)
        decrypted = multi_decrypt(encrypted, shift, key)
    else:
        print("Invalid choice.")
        return

    print("\nEncrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
