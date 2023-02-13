#If the bill was $150.00, split between 5 people, with 12% tip.
bill = float(input("What is the total bill ? "))
print(bill)
people = int(input("How many people do you what to split with ? "))
#print(people)
per = int(input("What is the tip % ? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
res = (bill/people)*(1+(per/100))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("%.2f" %res)
#Write your code below this line 👇