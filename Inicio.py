from builtins import print

number = 1
for row in range(2):
    for col in range(5):
        print(number,end=" ")
        number += 1
    print()
    print("Hello world")