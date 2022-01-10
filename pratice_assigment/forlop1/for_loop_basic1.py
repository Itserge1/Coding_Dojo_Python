for i in range(151):
    print(i)
for i in range(5, 1001, 5):
    print(i)
for i in range(100):
    if (i % 10 == 0):
        print("Coding Dojo")
        continue
    if (i % 5 == 0):
        print("Coding")
    else:
        print(i)
x = 0
for i in range(500001):
    if (i % 2 != 0):
        x = x + i
print(x)
for i in range(2018 , -1 , -4):
    if i > 0 :
        print(i)

lowNum = 2
highNum = 15
mult = 3
for lowNum in range(lowNum, highNum + 1):
    if lowNum % mult == 0:
        print(lowNum)
