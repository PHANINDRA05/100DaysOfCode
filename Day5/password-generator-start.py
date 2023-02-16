import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
res = ""
for i in range(1,nr_letters+1):
    res += random.choice(letters)

for i in range(1,nr_symbols+1):
    res += random.choice(numbers)

for i in range(1,nr_numbers+1):
    res += random.choice(symbols)
print(f"Password with order not randomised : {res}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

res = []
for i in range(1,nr_letters+1):
    res.append(random.choice(letters))

for i in range(1,nr_symbols+1):
    res.append(random.choice(numbers))

for i in range(1,nr_numbers+1):
    res.append(random.choice(symbols))
random.shuffle(res)

password = ""
for i in res:
    password += i
print(f"Password with order not randomised : {password}")

