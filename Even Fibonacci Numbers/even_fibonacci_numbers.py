def runTheNumbers():
    lastTwoSum = fibonacciSequence[-2] + fibonacciSequence[-1]
    fibonacciSequence.append(lastTwoSum)

fibonacciSequence = [1, 2]
limit = 4000000
sum = 0

while (fibonacciSequence[-2] + fibonacciSequence[-1]) <= limit:
    runTheNumbers()

for num in fibonacciSequence:
    if num % 2 == 0:
        sum += num

print(sum)