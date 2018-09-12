#This is used to randomize 16 digit alphanumerical codes to be used as passwords. To get a new password just click 'y' and repeat for more.

import random
def pswrd_maker():
    while True:
        print("Your password is " +
        ''.join(random.choice('0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm') for i in range(16)))
        another_pswrd = input("Would you like another password? ")
        while another_pswrd != 'y':
            if another_pswrd == 'n':
                return print("No password for you then.")
            else:
                print("Input not recongnized.")
                another_pswrd = input("Would you like another password? ")

def main():
    frst_pswrd = input("Would you like a new password? ")
    if frst_pswrd == 'y':
        pswrd_maker()
    else:
        print('Input not recognized')

if __name__ == '__main__':
    main()
