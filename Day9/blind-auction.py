logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
participants = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    participants[name] = bid
    restart = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if restart == 'no':
        break
max_bid = 0
for thing in participants:
    if participants[thing] > max_bid:
        max_bid = participants[thing]
        name = thing
print(f"The winner is {name} with a bid of ${max_bid}")

