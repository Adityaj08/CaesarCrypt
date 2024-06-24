class Cipher():

    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+={}[]/<>.,`~'*100
        

    def __crypt(self, mode):
        translated = ''
        for symbol in self.message:
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                translated = translated + self.LETTERS[num]
            else:
                translated = translated + symbol

        return translated

    def encrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')

    def decrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')

if __name__ == '__main__':
    cipher = Cipher()
    while True:
        try:
            choice = int(input("Choose The Mode\n\t1) encrypt\n\t2) Decrypt\n\t3) Exit\nEnter Choice: "))
        except ValueError:
            print("Error : Please enter integer (1, 2, 3)")
        match choice:
            case 1:
                message = input("Enter the message to encrypt: ")
                try:
                    key = int(input("Enter the Key: "))
                except ValueError:
                    print("Error : Please enter integer")
                print(f"\nThe encrypted Text is \n\"{cipher.encrypt(message, key)}\"")
            case 2:
                message = input("Enter the message to decrypt: ")
                try:
                    key = int(input("Enter the Key: "))
                except ValueError:
                    print("Error : Please enter integer")
                print(f"\nThe Decrypted Text is \n\"{cipher.decrypt(message, key)}\"")
            case 3:
                exit(0)
            case _:
                print("Enter a valid choice: ") 
