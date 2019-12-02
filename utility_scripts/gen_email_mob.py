# Generate email addresses and numbers
import random

alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"

emails = []
for _ in range(2000):
	# Generate random string of format [a-z0-9]@[a-z0-9].[a-z0-9]
	# to look like an email id
	k = random.randint(3,7)
	email = "".join(random.choices(alphanum, k = k))
	k = random.randint(2,3)
	email += "@" + "".join(random.choices(alphanum, k = k)) 
	k = random.randint(2,3)
	email += "." + "".join(random.choices(alphanum, k = k))
	emails.append(email)

numbers = []
for _ in range(500):
	# Generate a random number n between 5 and 10
	n = random.randint(5,10)
	# Genereate random number of random length n
	numbers.append("".join([str(random.randint(0,9)) for i in range(n)]))
# Write fake emails and numbers to file.
with open("fake_emails_nums.txt", "a") as f:
	print(*emails, sep="\n", file=f)
	print(*numbers, sep="\n", file=f)