multiplicand = 999
multiplier = 999
palindromes = []
foundPalendrome = False

while multiplicand > 0:
    product = multiplicand * multiplier
    print(f"product of {multiplicand} and {multiplier} is: {product}")
    stringProductForward = list(str(product))
    stringProductReverse = list(stringProductForward[::-1])
    if stringProductForward == stringProductReverse:
        print("found one")
        palindromes.append(product)
    multiplier -= 1
    if multiplier < 1:
        multiplicand -= 1
        multiplier = multiplicand

palindromes.sort()
print(palindromes[-1])