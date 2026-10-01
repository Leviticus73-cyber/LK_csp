#LK6, Caaesar Cipher
de = input("Would you like to (E)ncrypt or (D)ecrypt a message?:").upper()
word = input("Enter your message:")
mo = input("Enter a shift amount:").isnumeric()

def cae(message, shift):
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num = num + shift
            if letter.isupper():
                if num > 90:
                    num = num - 26
                if num < 65:
                    num = num+26
            else:
                if num > 122:
                      num = num - 26
                if num < 65:
                   num = num + 26
            numb = chr(num)
            let = numb
        return let
if de == "E":
    n = cae(word, mo)
    print("message is,", n)
if de == "D":
    n = cae(word,-mo)
    print("message is,", n)