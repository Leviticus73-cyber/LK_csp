#LK6, Caaesar Cipher
de = input("Would you like to (E)ncrypt or (D)ecrypt a message?:")
word = input("Enter your message:")
mo = input("Enter a shift amount:")

def shift(message, move):
    return (message + move)
if de == "E" or "e":
    print(shift(word,mo))