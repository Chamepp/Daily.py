import random
import string
import csv
import progressbar

# Email Counts
def getcount():
	rownums = input("How many email addresses?: ")
	try:
		rowint = int(rownums)
		return rowint
	except ValueError:
		print ("Please enter an integer value")
		return getcount()

# Create Email
def makeEmail():
	extensions = ['com','net','org','gov']
	domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

	winext = extensions[random.randint(0,len(extensions)-1)]
	windom = domains[random.randint(0,len(domains)-1)]

	acclen = random.randint(1,20)

	winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

	finale = winacc + "@" + windom + "." + winext
	return finale

# Data
howmany = getcount()
counter = 0
emailarray = []


# Complete Process
print ("Creating email addresses...")
print ("Progress: ")

prebar = progressbar.ProgressBar(maxval=int(howmany))

for i in prebar(range(howmany)):
	while counter < howmany:
		emailarray.append(str(makeEmail()))
		counter = counter+1
		prebar.update(i)
	
print ("Creation completed.")

# Output
for i in emailarray:
    print(i)
