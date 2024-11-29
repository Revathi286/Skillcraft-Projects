def caesar_cipher(message, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift
        
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
            
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Encrypt a message from a file")
    print("4. Decrypt a message from a file")

    choice = input("Enter your choice (1-4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid option. Please choose a number between 1 and 4.")
        return
    
    if choice in ['1', '2']:
        message = input("Enter your message: ")
    else:
        file_path = input("Enter the file path: ")
        try:
            with open(file_path, 'r') as file:
                message = file.read()
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            return
    
    shift = int(input("Enter shift value (positive or negative integer): "))
    
    if choice == '1':
        result = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message: {result}")
    elif choice == '2':
        result = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {result}")
    elif choice == '3':
        result = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message from file: {result}")
    elif choice == '4':
        result = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message from file: {result}")
    
    save_choice = input("Would you like to save the result to a file? (y/n): ").lower()
    if save_choice == 'y':
        output_path = input("Enter the output file path: ")
        try:
            with open(output_path, 'w') as file:
                file.write(result)
            print(f"Result saved to {output_path}")
        except IOError:
            print("Error saving the file. Please check the file path.")

if __name__ == "__main__":
    main()
