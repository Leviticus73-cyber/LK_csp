#LK6, Caaesar Cipher
while True:
    de = input("Would you like to (E)ncrypt or (D)ecrypt a message?:").upper()
    word = str(input("Enter your message:"))
    mo = input("Enter a shift amount:")
    mmo = mo * -1

    def shift(message, move):
        return (message + move)
    if de == "E":
        print(shift(word,mo))
        break
    elif de == "D":
        print(shift(word,mmo))
        break
    else:
        print("try again")