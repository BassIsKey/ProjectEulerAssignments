def multipleOf3or5(num):
    if num % 3 == 0 or num % 5 == 0:
        affirmativesList.append(num)

affirmativesList = []
sum = 0

for num in range(0,1000):
    multipleOf3or5(num)

for element in affirmativesList:
    sum = sum + element

print(sum)