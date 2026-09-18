#LK6, your budget

income = float(input("what is your monthly income:$"))

rent = float(input("what is your rent monthly:$"))

util = float(input("what do you pay monthly for utilities:$"))

groc = float(input("what do yo pay for groceries monthly:$"))

tran = float(input("what is your monthly payment to travel:$"))


print(f"your rent is {rent/income*100}% of your income")

print(f"your utilities is {util/income*100}% of your income")

print(f"your groceries is {groc/income*100}% of your income")

print(f"your transportation is {tran/income*100}% of your income")

print(f"this is your spending money for the month: ${income-rent-util-groc-tran}")