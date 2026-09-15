#LK6, fixing input

# when you want a number

while True:
    try:
        name = int(input("tell me your name:"))
        break
    except:
        print("that isn't a a name")
    
print(f"hi" ,name ,", how are you")







