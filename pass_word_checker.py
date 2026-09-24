#LK6, pass word checker
print ("your Password must contain least have 8 characters long, needs at least one Uppercase, at least one lowercase, needs at least one Number, and must have at least one Symbol")
al8c = False
up = False
low = False
num = False
sym = False

score = 0
pas = input("type in your Password:")
lent =len(pas)




for letter in pas:
    if lent >= 8:
        al8c = True

if any(letter.isupper() for letter in pas):
    up = True

if any(letter.islower() for letter in pas):
    low = True

if any(letter.isdigit() for letter in pas):
    num = True

if any(letter in "!@#$%^&*" for letter in pas):
    sym = True

    if al8c == True:
        score += 1

    if up == True:
     score += 1

    if low == True:
        score += 1

    if num == True:
        score += 1

    if sym == True:
        score += 1
    
    if score == 5:
        strong = "strong"

    elif score >= 3:
        strong = "medium"

    else: 
        strong = "weak"

print("\nPassword:", pas) 
print("Length:", al8c)
print("Uppercase:", up)
print("Lowercase:", low)
print("Number:", num)
print("Symbol:", sym)
print("Strength:", strong)

