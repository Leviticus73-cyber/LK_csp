#LK6, Caaesar Cipher
de = input("Do you want to (E)ncode or (D)ecode: ").upper()
words = input("What is your message: ")
mo = int(input("How much do you want to shift: "))
def caeser_shift(message, shift):
    newmessage = ""

    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num = num + shift

            if letter.isupper():
                if num > 90:
                    num = num - 26
                if num < 65:
                    num = num + 26
            else:
                if num > 122:
                    num = num - 26
                if num < 97:
                    num = num + 26

            letter = chr(num)

        newmessage = newmessage + letter

    return newmessage

if de == "E":
    message = caeser_shift(words, mo)
    print("Your encrypted message is:", message)
elif de == "D":
    message = caeser_shift(words, -mo)
    print("Your decrypted message is:", message)
