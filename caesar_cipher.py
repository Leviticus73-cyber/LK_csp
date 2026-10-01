#LK6, Caaesar Cipher
de = input("Would you like to (E)ncrypt or (D)ecrypt a message?:").upper()
word = input("Enter your message:")
mo = input("Enter a shift amount:").isnumeric()


if de == "E":
    for letter in word:
        if letter.isalpha():
            num = ord(letter)
        new =chr(mo + num)

        print(new)
if de == "D":
    for letter in word:
        if letter.isalpha():
            num = ord(letter)
        new = chr(num - mo)
        print(new)
