highNumber = 100
numbersList = list(range(highNumber + 1))

sumOfSquares = 0
for number in numbersList:
    squaredNumber = number ** 2
    sumOfSquares += squaredNumber

sumOfNumbers = 0
for number in numbersList:
    sumOfNumbers += number
squareOfSum = sumOfNumbers ** 2

difference = squareOfSum - sumOfSquares

print(difference)