# Generate email addresses and numbers
import random

alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"

emails = []
for _ in range(2000):
	k = random.randint(3,7)
	email = "".join(random.choices(alphanum, k = k))
	k = random.randint(2,3)
	email += "@" + "".join(random.choices(alphanum, k = k)) 
	k = random.randint(2,3)
	email += "." + "".join(random.choices(alphanum, k = k))
	emails.append(email)

numbers = []
for _ in range(500):
	n = random.randint(5,10)
	numbers.append("".join([str(random.randint(0,9)) for i in range(n)]))
with open("fake_emails_nums.txt", "a") as f:
	print(*emails, sep="\n", file=f)
	print(*numbers, sep="\n", file=f)