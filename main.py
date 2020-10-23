import RSA02
import steg02

def main():

    choose_again = input('Do you want to generate a new public and private key? (y or n) ')
    if choose_again == 'y':
        RSA02.chooseKeys()

    instruction = input('Would you like to encrypt or decrypt (e or d) ')
    if instruction == 'e':
        message = input('What would you like to encrypt?\n')
        option = input('do you want to encrypt using your own public key? (y or n) ')

        if option == 'y':
            cipher = RSA02.encrypt(message)

            img = input("Enter image name (with extension): ")
            new_img_name = input("Enter the name of new image (with extension): ")
            steg02.encode(cipher, img, new_img_name)

            print('Encrypting...')
            print('Encrypted message is: ', cipher)
            
        else:
            file_option = input('Enter the file name that stores the public key: ')
            cipher = RSA02.encrypt(message, file_option)

            img = input("Enter image name (with extension): ")
            new_img_name = input("Enter the name of new image (with extension): ")
            steg02.encode(cipher, img, new_img_name)

            print('Encrypting...')
            print('Encrypted message is: ', cipher)

    elif instruction == 'd':
        print('What would you like to decrppt?\n')

        img = input('Enter image name (with extension): ')

        print('Decrypting...')

        cipher = steg02.decode(img)

        message = RSA02.decrypt(cipher)

        print(message)

    else:
        print('This is not a valid instruction.')

if __name__=='__main__':
    main()



