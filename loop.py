#LK6, Loops

count = 1


while count <= 10:
    print (count)
    count += 1

    break



import random

goose = random.randint(1,100)
duck = 1

while True:
    print("Duck!")
    duck += 1
    if duck == goose:
        break
print("Goose!")
print(duck)


sibling =["caleb", "marissa", "chloe", "kam", "remmy", "andy", "daisy", "unknown"]


print (sibling[5])
print(sibling)
sibling.append("someone")
sibling.insert(0,"levi")
print(sibling)

print(sibling.pop(7))
sibling.pop(7)


print(sibling)

for number in range (1,11,1):
    print(number)



for sibling in sibling:
    print(sibling + " king")