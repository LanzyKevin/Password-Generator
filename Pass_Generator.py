import secrets
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""

pwLen = int(input("How long does the password need to be? "))
minUpper = int(input("Minimum Uppercase letters? "))
minLower = int(input("Minimum Lowercase letters? "))
minDigits = int(input("Minimum Numbers? "))
minSpec = int(input("Minimum Special characters? "))

for i in range(minUpper):
  password += "".join(random.choice(secrets.choice(upper)))

for i in range(minLower):
  password += "".join(random.choice(secrets.choice(lower)))

for i in range(minDigits):
  password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
  password += "".join(random.choice(secrets.choice(special)))

remaining = pwLen - minUpper - minLower - minDigits - minSpec

for i in range(remaining):
  password += "".join(random.choice(secrets.choice(allChars)))

password = list(password)
random.shuffle(password)
print("".join(password))