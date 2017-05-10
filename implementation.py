'''
Inputs a file name as a string, reads from the file and returns a list of words as string values
'''
def create(puzzle):
    result = []
    fileInput = open(puzzle)

    for letter in fileInput:
        result.append(letter.strip())

    fileInput.close()

    return result

'''
Reads the equation and returns a list of numbers that are not found in the equation and these numbers
become the possible candidates for assignment
'''
def guess(equation):
    nums = [i for i in range(10)]
    for word in equation:
        for letter in word:
            if letter.isdigit() and int(letter) in nums:
                nums.remove(int(letter))

    return nums

'''
Takes the equation and returns a new equation after a certain letter is replaced by a number, this
is determined by the decideLetter function.
'''
def replace(equation, number):

    def decideLetter(equation):
        width = len(equation[-1])
        for i in range(width):
            for word in equation:
                if len(word)>i and word[-i-1].isalpha():
                    return word[-i-1]

    target = decideLetter(equation)
    result = []
    for word in equation:
        updatedWord = ""
        for l in word:
            if l == target:
                updatedWord += str(number)
            else:
                updatedWord += l
        result.append(updatedWord)

    return result



'''
Counts how many digits in an equation have been changed from letters to numbers.
'''
def numDigits(equation):
    width = len(equation[-1])
    result = 0

    for digit in range(1, width+1):
        numerated = True
        for word in equation:
            if len(word) >= digit and (not word[-digit].isdigit()):
                numerated = False
                break
        if not numerated:
            break

        result += 1

    return result

'''
Determines if the numbers chosen comply with the rules of addition, and all the digits must be numbers.
'''
def validateDigits(equation,n):
    width = len(equation[-1])
    sum = 0

    if n == 0:
        return True

    for word in equation[:-1]:
        sum += int(word[-n:])

    if n == width:
        return sum == int(equation[-1][-n:])

    return (sum%(10**n)) == int(equation[-1][-n:])

'''
Checks if equation is valid and there are no letters left as well and no zeros as first digits.
'''
def accept(equation):
    nums = []

    for word in equation:
        if not word.isdigit():
            return False
        if word[0] == "0":
            return False
        nums.append(int(word))
    s = sum(nums[:-1])

    return s == nums[-1]

'''
Checks if a word begins with zero or if there are numbers that have been rejected then return True.
'''
def reject(equation):

    for word in equation:
        if word[0]=="0":
            return True

    if not validateDigits(equation,numDigits(equation)):
        return True

    return False

'''
This is the backtracking portion. Recursively call the possible guesses
from the constraints and if the solution is found and return it.
Otherwise return empty set if no solution is possible.
'''
def solve(equation):

    if accept(equation):
        return equation
    if reject(equation):
        return []

    possibles=guess(equation)

    for i in possibles:
        newTry = replace(equation,i)

        if solve(newTry):
            return solve(newTry)

    return []

'''
Prints the list in an organized manner
'''
def display(equation):
    width = len(equation[-1]) + 2
    for w in equation[:len(equation) - 2]:
        print(w.rjust(width))

    last = equation[-2]
    display = "+" + last.rjust(width - 1)

    print(display)
    print("-" * width)
    print(equation[-1].rjust(width))
