import random
import string
#random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(3))
message=input("Enter you message")
words = message.split()
coded_words = []
for i in words:
    if len(i) > 2:
        coded=''.join(random.choice(string.ascii_letters) for _ in range(3))+ i[1:]+ i[0]+ ''.join(random.choice(string.ascii_letters) for _ in range(3))
        coded_words.append(coded)
    elif len(i)==2:
        coded=i[1]+i[0]
        coded_words.append(coded)
    else:
        coded=i
        coded_words.append(coded)
final = ' '.join(coded_words)
print(final)