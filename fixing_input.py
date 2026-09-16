#LK6, fixing input

# when you want a name

while True:
    name = input("tell me your 1st name:").title().strip()
    if name.isnumeric():
            print("that isn'ts a name silly")
    elif " " in  name:
        print("I ask for your frist name")
    else:
        print (f"hi",name," how are you")
        break





