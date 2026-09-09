def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

# ----------------------------------------------------
# 🖥️ INTERACTIVE USER CLI ENGINE
# ----------------------------------------------------
def run_cli():
    print("=" * 40)
    print("      🔐 CAESAR CIPHER CLI ENGINE 🔐      ")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit App")
        
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == '3':
            print("\nGoodbye! Stay secure. 🚀")
            break
            
        if choice not in ['1', '2']:
            print("❌ Invalid option. Please enter 1, 2, or 3.")
            continue
            
        user_text = input("\nEnter your message: ")
        
        # Guard rail for numeric shift input
        try:
            user_shift = int(input("Enter shift number (1-25): "))
        except ValueError:
            print("❌ Error: Shift must be a whole number.")
            continue

        if choice == '1':
            result = encrypt(user_text, user_shift)
            # If our internal guard rail strings are returned, show it as an error
            if "must be" in str(result):
                print(f"❌ {result}")
            else:
                print(f"\n🔒 Encrypted Text: {result}")
                
        elif choice == '2':
            result = decrypt(user_text, user_shift)
            if "must be" in str(result):
                print(f"❌ {result}")
            else:
                print(f"\n🔓 Decrypted Text: {result}")
        
        print("-" * 40)

# Start the interactive app
if __name__ == "__main__":
    run_cli()