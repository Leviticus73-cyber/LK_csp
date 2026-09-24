#LK6, pass word checker
print ("your Password must contain least have 8 characters long, needs at least one Uppercase, at least one lowercase, needs at least one Number, and must have at least one Symbol")
al8c = False
up = False
low = False
num = False
sym = False
symbols = "!@#$%^&*"
score = 0
pas = input("type in your Password:")
lent =len(pas)





if lent >= 8:
    al8c = True

for letter in pas:
    if letter.isupper():
        up==True
    if letter in symbols:
        sym==True
    if letter.islower():
        low==True
    if letter.isnumeric():
        num==True
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
print ("your password is "+strong+".")