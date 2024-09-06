import random

friends = ["James", "John", "Thomas", "Mary", "Sally", "Bob", "George"]

payer = random.randint(0, len(friends) - 1)

print(f"The person who will pay for the lunch will be {friends[payer]}")
print(f"The person who will pay for the lunch will be {random.choice(friends)}")
