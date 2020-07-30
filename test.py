import string
import random

x= [''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + 'c', k=8))  for _ in range(5000)]
print(x)