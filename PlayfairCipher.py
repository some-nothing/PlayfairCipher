import function as Encrypt

def main():
    key = "playfair example"
    chiper = Encrypt.get_chiper(key)
    
    plaintext = 'Hide the gold in the tree stump'
    plaintext = Encrypt.plaintext_process(plaintext)

    encryptext = Encrypt.encrypt(plaintext, chiper).upper()
    print([encryptext[i:i+2] for i in range(0, len(encryptext), 2)])

if __name__ == '__main__':
    main()