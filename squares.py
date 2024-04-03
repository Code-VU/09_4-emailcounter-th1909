di = {}

number: int = 1
while number <= 15:
    di.update({number : (number ** 2)})
    number += 1

print(di)