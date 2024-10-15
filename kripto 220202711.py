def encrypt(text, shift):
    result = ""
    
    # Enkripsi pesan
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetical characters stay the same
        else:
            result += char
    
    return result

def decrypt(text, shift):
    result = ""
    
    # Dekripsi pesan
    for i in range(len(text)):
        char = text[i]
        
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Non-alphabetical characters stay the same
        else:
            result += char
    
    return result

def generate_access_code(text):
    # Membuat kode akses berdasarkan total nilai ASCII dari semua karakter dalam teks
    access_code = sum(ord(c) for c in text) % 100
    return access_code

def open_message_with_access_code(encrypted_message, shift, correct_access_code):
    entered_code = int(input("Masukkan kode akses untuk membuka pesan: "))
    
    # Verifikasi kode akses
    if entered_code == correct_access_code:
        # Jika kode akses benar, tampilkan pesan yang sudah didekripsi
        decrypted_message = decrypt(encrypted_message, shift)
        print(f"\nPesan terenkripsi: {encrypted_message}")
        print(f"Pesan terdekripsi: {decrypted_message}")
    else:
        print("Kode akses salah! Anda tidak bisa membuka pesan ini.")

def menu():
    encrypted_message = None
    shift_used = None
    access_code = None
    
    print("=== Program Caesar Cipher ===")
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    print("3. Dapatkan Kode Akses")
    print("4. Buka Pesan dengan Kode Akses")
    print("5. Keluar")
    
    while True:
        choice = input("\nPilih menu (1/2/3/4/5): ")
        
        if choice == '1':
            text = input("Masukkan pesan yang ingin dienkripsi: ")
            shift = int(input("Masukkan pergeseran (shift): "))
            encrypted_message = encrypt(text, shift)
            shift_used = shift
            print(f"Pesan terenkripsi: {encrypted_message}")
        
        elif choice == '2':
            text = input("Masukkan pesan yang ingin didekripsi: ")
            shift = int(input("Masukkan pergeseran (shift): "))
            decrypted_message = decrypt(text, shift)
            print(f"Pesan terdekripsi: {decrypted_message}")
        
        elif choice == '3':
            # Pastikan ada pesan yang terenkripsi sebelum menghasilkan kode akses
            if encrypted_message is None or shift_used is None:
                print("Enkripsi pesan terlebih dahulu sebelum mendapatkan kode akses!")
            else:
                access_code = generate_access_code(encrypted_message)
                print(f"Kode akses untuk membuka pesan: {access_code}")
        
        elif choice == '4':
            # Pastikan pesan sudah di-enkripsi dan kode akses telah dibuat sebelum membuka
            if encrypted_message is None or shift_used is None or access_code is None:
                print("Tidak ada pesan terenkripsi atau kode akses yang tersedia. Silakan enkripsi pesan dan dapatkan kode akses terlebih dahulu.")
            else:
                open_message_with_access_code(encrypted_message, shift_used, access_code)
        
        elif choice == '5':
            print("Keluar dari program...")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Jalankan program
menu()
