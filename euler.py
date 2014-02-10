#Exercise to prompt user for a name, then print the reverse
#Later note: you can also just do foo[::-1]
def promptName():
    foo = input("Please enter your name: ")
    print(reverseString(foo))    

def reverseString(stringToReverse):
    length = len(stringToReverse)
    output = ""
    for x in stringToReverse:
        length = length -1
        output = output + stringToReverse[length]
    return output
#Exercise to prompt user for a sentence, then print each word on a new line
def promptSentence():
    foo = input('Please enter a sentence: ')
    tokenizeString(foo)

def tokenizeString(inp):
    foo = inp.split()
    for word in foo:
        print(word)

#Exercise to prompt user for a number, then create a right isosceles triangle
def promptHeight():
    foo = input("Enter a height value: ")
    isoscelizeThis(int(foo))
    
def isoscelizeThis(inp):
    for x in range(inp +1):
        print("*"*x)

#Extension of above exercise to build a sideways triangle instead
def promptHeight2():
    foo = input("Enter an integer value: ")
    sidewaysThis(int(foo))

import math

def sidewaysThis(inp):
    height = inp * 2 - 1
    counter = 0
    for x in range(height):
        if (x>inp-1):
            counter = counter - 1
        else:
            counter = counter + 1
        print("*"*counter)

#Extended exercise to print a rightside up triangle
          
def promptHeight3():
    foo = input("Enter an integer: ")
    rightwaysThis(int(foo))

def rightwaysThis(inp):
    maxWidth = inp * 2 - 1
    for x in range(inp):
        print(" "*(inp - x -1) + "*" * (2*x+1))
        
#Exercises in program flow

def coreFunction():
    userInput = input("Enter command: ")
    while (userInput!=("Q") and userInput!=("q")):        
        if (userInput==("1")):
            firstFunction()
        elif (userInput==("2")):
            secondFunction()
        elif (userInput==("3")):
            thirdFunction()
        userInput = input("Enter command: ")

def firstFunction():
    print("First function")
    
def secondFunction():
    print("Second function")
    
def thirdFunction():
    print("Third function")

#Project Euler Exercises==================================================

#This sums all multiples of 3 and 5 below 1000

def SumMultiples():
    total = 0
    for x in range(1000):
        if(x%3==0 or x%5 ==0):
            total = total + x
    print(total)

#SumMultiples()

#This is a basic recursive Fib function

def FindFib(term):
    term = int(term) #just in case
    if(term<3):
        return 1
    else:
        return FindFib(term-1) + FindFib(term-2)

#This is the exercise: find the sum of all even VALUED Fib terms that do not exceed 4 million

def FindEvenFibSum(termValueLimit):
    runningTotal = 0
    lastFib = 0
    fibIndex = 1
    listOfFibs = []
    while(lastFib<termValueLimit):
        if(lastFib%2 == 0):
            runningTotal += lastFib
            listOfFibs.append(lastFib)
        lastFib = FindFib(fibIndex)
        fibIndex += 1
        
    print("Last even fib value under " + str(termValueLimit) + " is: " + str(listOfFibs[len(listOfFibs)-1]))
    print(listOfFibs)
    print("The sum is: " + str(runningTotal))

#FindEvenFibSum(4000000)

#This exercise is to find the largest prime factor (singular) in a large number (600851475143)

#A coarse way to figure out whether a number is prime
def IsThisNumberPrime(number):
    number = int(number) #I just don't like to mess with floats for now

    if(number<0):
        print("I'm not checking values below 0")
        return
    elif(number==1):
        return False
    elif(number%2==0 and number!=2):
        return False          

    stopPoint = int(math.sqrt(number)) #Once we get to the point of x*x, we're done checking

    count = 3
    while(count<=stopPoint):
        if (number % count ==0 and count<number):
            return False   
        count += 2      

    return True

#Okay, so we want to look for factors and when we find them, add them to the list, divide the big number by it and search the resultant for more factors

def FindPrimeFactors(number):
    number = int(number)
    
    if(number<1):
        print("I'm not checking values below 1")
        return
    
    currentList = []

    currentFactor = 2
    while(number>1):
        if (number%currentFactor == 0):
            currentList.append(currentFactor)
            number /= currentFactor
            if(currentFactor!=1):
                currentFactor -= 1 #if we're not at the identity element, we want to check for repetitions, like 1*2*2*2
        currentFactor += 1
    return currentList

#print(FindPrimeFactors(600851475143))

#This exercise finds the largest pallindrome from the product of two three-digit numbers

#Start off with a way to check whether the number is a pallindrome
def IsThisNumberAPallindrome(number):
    stringNum = str(number)
    length = len(stringNum)
    halfLen = int(length/2)
    
    for x in range(halfLen):
        if (stringNum[x] != stringNum[length-x-1]):
            return False
        
    return True

#Now we just need to find a reasonably efficient way to iterate through numbers to get the largest pallindrome
def PallindromeFromTwoThreeDigits():
    pallindromes = []
    for x in range(100,1000):
        for y in range(100, 1000):
            if (IsThisNumberAPallindrome(x*y)):
                pallindromes.append(x*y)

    return max(pallindromes)

#print(PallindromeFromTwoThreeDigits())

#This exercise attempts to find the smallest number that can be evenly divided (no remainder) by the numbers from 1 to 20
#For any given number range 1-n, we only need to check n/2 - n since everything below n/2 divides into that range evenly somewhere

def BuildRange(num):
    """This builds a list of numbers that we need to create prime factorization for."""
    half = int(num/2)
    currSet = []
    for x in range(half, num+1):
        currSet.append(x)
    return currSet #So if we had 1-21, we'd save the numbers 10-20 to do prime factorization later

def FindRangePrimeFactors(upper):
    """Takes a number for an upper range limit (starting with 1) and finds the least-common-multiple of it"""
    currSet = BuildRange(upper)
    allPrimeFactors = []
    greatestPrimeFactors = []
        
    for num in currSet:
        foo = FindPrimeFactors(num) #Creates a list of prime factor lists, we'll need this in a bit
        print(str(num) + ": " + str(foo))
        allPrimeFactors.append(foo) 
    return allPrimeFactors

#Technically, we could write a function that searches each list for the greatest number of prime factors of each, but I just did it by hand.

#FindRangePrimeFactors(20)

#This exercise finds the difference between the sum of squares and the square of the sum of the first 100 natural numbers

def SumOfSquares(limit):
    runningTotal=0
    for x in range(1, limit+1):
        runningTotal += math.pow(x, 2)

    return runningTotal

def SquareOfSum(limit):
    foo = int(math.fsum(range(1, limit+1))) #the sum of 1 to n
    return math.pow(foo, 2)

#print(SquareOfSum(100) - SumOfSquares(100))

#This exercise is just to find the 10001th prime number, though we'll go ahead and make it a more general case
def FindNthPrime(number):
    potentialPrime = 3
    lastPrime = 3
    while(number-1>0):
        if(IsThisNumberPrime(potentialPrime)):
            lastPrime = potentialPrime
            number -= 1 
            print("Left: " + str(number))
        potentialPrime += 2
    return lastPrime

#print(FindNthPrime(10001)) #So we know that 2 is the only even prime, so to speed things up, start at the 2nd prime (3) and increment by 2

#This exercise finds the largest product in a particular 1000-digit number that I won't list in the comment here

def ProductFromSlice(number):
    """Takes as input a number and outputs the product as though each digit were a number."""
    numString = str(number) #Because the exercise number is so lengthy, it's really kept as a string, but this is just in case
    product = 1
    for x in numString:
        product *= int(x)
        
    return product

def FindMaxProduct():
    """Works on a huge number, really a string, and finds the largest possible product of any five consecutive digits."""
    lastMax = 0
    currentMax = 0
    sliceStart = 0
    sliceEnd = 5
    value= "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

    length = len(value)
    while(sliceEnd<length+1):
        currentMax = ProductFromSlice(value[sliceStart:sliceEnd])
        if (currentMax > lastMax): lastMax = currentMax
        sliceStart += 1
        sliceEnd +=1
    return lastMax

#print(FindMaxProduct())

#This exercise attempts to find the Pythagorean triplet whose sum = 1000, and then outputs the product of the three numbers.

def BruteForceTrip(number):
    """Takes as input a number, then attempts to simply find sets of three different numbers which sum to 1000."""
    currentList = []
    for x in range(number+1):
        for y in range(1, number+1):
            for z in range(2, number+1):
                if (x < y and y < z and x + y + z == number):
                    currentList.append([x,y,z])
    return currentList

def TestForPythTriple(numList):
    """Takes as input a list of numbers, 3 at a time, and tests whether the elements are Pythagorean triplets."""
    currentList = []
    for miniList in numList:
        a = miniList[0]
        b = miniList[1]
        c = miniList[2]
        if(math.pow(a,2) + math.pow(b,2) == math.pow(c,2)):
            currentList.append(miniList)
    return currentList

#val = BruteForceTrip(1000)
#foo = TestForPythTriple(val)
#print(foo)

#This exercise finds all primes below an arbitrary value and sums them together
def FindAllPrimesBelow(number):
    currentPrimes = []
    for x in range(number):
        if(IsThisNumberPrime(x)):
            currentPrimes.append(x)
            print(x)
    return currentPrimes

#foo = FindAllPrimesBelow(2000000)
#print("_____________________")
#print(int(math.fsum(foo)))

#This exercise takes a huge grid of numbers and tries to find the largest product of any four in a row (in any direction)

def SetupNumberLists():
    """This function generates the list of lists of numbers to be scanned."""
    
    r1 = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]    
    r2 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00]
    r3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]    
    r4 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
    r5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
    r6 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
    r7 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
    r8 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
    r9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
    r10 = [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95]
    r11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
    r12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57]
    r13 = [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
    r14 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
    r15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
    r16 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
    r17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
    r18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
    r19 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
    r20 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]


    return [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]
    
#print(foo[0][1:])

def ScanDirection(nums, row, col, direction):
    """Takes as input the list generated above and naivly scans in a particular direction, assuming that it won't go out of bounds"""
    f1 = nums[row][col]
    if (direction=="down"):
        f2 = nums[row+1][col]
        f3 = nums[row+2][col]
        f4 = nums[row+3][col]

        return f1*f2*f3*f4
    elif (direction=="right"):
        f2 = nums[row][col+1]
        f3 = nums[row][col+2]
        f4 = nums[row][col+3]
        
        return f1*f2*f3*f4
    elif (direction=="dright"):
        f2 = nums[row+1][col+1]
        f3 = nums[row+2][col+2]
        f4 = nums[row+3][col+3]

        return f1*f2*f3*f4
    else: #down left
        f2 = nums[row+1][col-1]
        f3 = nums[row+2][col-2]
        f4 = nums[row+3][col-3]

        return f1*f2*f3*f4

def ScanEntireList():
    """Scans the number field in three passes doing a simple compare/replace to find the max value."""
    nums = SetupNumberLists()
    lastMax = 0
    currentMax = 0
    width = len(nums[0])
    height = len(nums) #should be 20 items of the list type...

    #Scan all options to the right
    for row in range(0, height):
        for col in range(0, width-3):               
            currentMax = ScanDirection(nums, row, col, "right")
            if (currentMax > lastMax): lastMax = currentMax
    #Scan all options down
    for row in range(0, height-3):
        for col in range(0, width):               
            currentMax = ScanDirection(nums, row, col, "down")
            if (currentMax > lastMax): lastMax = currentMax
    #Scan diagonally down right
    for row in range(0, height-3):
        for col in range(0, width-3):               
            currentMax = ScanDirection(nums, row, col, "dright")
            if (currentMax > lastMax): lastMax = currentMax        
    for row in range(0, height-3):
        for col in range(3, width):
            currentMax = ScanDirection(nums, row, col, "meh")
            if (currentMax > lastMax): lastMax = currentMax 

    return lastMax

#foo = ScanEntireList()
#print(foo)

#This exercise attempts to find the first triangle number with over five hundred divisors

def GetStandaloneTriangleNumber(seed):
    """Just a small method generate the triangle value for a particular number."""
    return int(math.fsum(range(seed+1)))

def GetTriangleNumber(seed, lastValue):
    """Slight variant of the above, which naiivly takes the last triangle number and simply adds the next value."""
    return seed + lastValue

def CountAmountOf(numList, value):
    """Takes a list of numbers, scans for the input value and returns how many of that number are in the list."""
    count = 0
    if(value in numList):
        for x in numList:
            if (x==value):
                count += 1
    return count
    
def BuildPrimeFactorAndPowerList(primeFactorsList):
    """Takes as input a list of prime factors generated by FindPrimeFactors() and creates tuples to denote the max power of each factor."""
    currList = []
    print(primeFactorsList)
    for x in primeFactorsList:
        amount = CountAmountOf(primeFactorsList, x)
        print("Amount of " + str(x) + ": " + str(amount))
        foo = Contains(currList, x)
        if(foo==False or foo==None): #If we haven't seen this number before
            print("Adding in a new value for " + str(x) + ": " + str(amount))
            currList.append([x, amount])

    print(currList)
    return currList
                

def Contains(numList, element):
    """Takes a list of lists and search each nested list for the element. o_o"""
    for pair in numList:
        return element in pair
        
def RepackagePrimes(primeList):
    """Takes a list of prime pairs, the power of each, then builds a list of numbers spawned from them.  So 2^2 would be 1 2 4."""
    currList = []
    for x in primeList:
        values = []
        power = x[1]
        while(power>0):
            values.append(int(math.pow(x[0], power)))
            power -= 1
        currList.append(values)
    return currList

def GenerateDivisors(num):
    """Takes a number, then generates its divisors using the functions we created above."""
    rawPrimes = FindPrimeFactors(num)
    arrangedPrimes = BuildPrimeFactorAndPowerList(rawPrimes)
    repackagedFactors = RepackagePrimes(arrangedPrimes)

    divisorList = []
    index1 = 1
    index2 = 1
    for multiples in repackagedFactors:
        for element in multiples:
            divisorList.append(element)
            for otherMultiples in repackagedFactors[index1:]:
                for otherElement in otherMultiples:
                    divisorList.append(element*otherElement)
            index2 += 1
        index1 += 1

    core = 1
    count = 1
    for x in rawPrimes:
        foo = x in rawPrimes[count:]
        if(foo==False):
            core *= x
        count += 1
        
    divisorList.append(1)
    divisorList.sort()
    return divisorList

def FindNumOfDivisors(num):
    """Turns out that the working of the problem means we don't care what the divisors are, just how many.  Makes life easier."""
    rawPrimes = FindPrimeFactors(num)
    totalProduct = 1
    oldPrimes = []
    for prime in rawPrimes:
        if((prime in oldPrimes)==False): #If we haven't seen this prime before
            oldPrimes.append(prime)
            amount = CountAmountOf(rawPrimes, prime) #Count how many times it's a factor
            amount += 1
            totalProduct *= amount #Then multiply a running total by that number
    return totalProduct

def GetDivisors(num):
    """Takes as input an integer, then returns a list of all of its divisors."""
    half = int(num/2) #once we reach this point, not need to check for more. Just be sure to append the number itself after
    
    divisors = []

    for x in range(1, half+1):
        if (num%x==0):
            divisors.append(x)

    divisors.append(num)
    return divisors

#So this is just the simple iterator one, whee...
def BruteForceFindMaxTriangleDivisors(limit):
    divisors = 1
    count = 1
    triVal = 0
    while(divisors<limit):        
        triVal = GetTriangleNumber(count, triVal)
        divisors = FindNumOfDivisors(triVal)

        print("Index: " + str(count))
        print("Triangle value: " + str(triVal))
        print("Number of dDivisors: " + str(divisors))

        count += 1

    return triVal

#BruteForceFindMaxTriangleDivisors(500)

#This exercise prints the first ten digits of the sum of 100 50-digit numbers.  However, the numbers are in a text file and need to be formatted first.

def SumFileLines():
    """Sums up the lines of numbers in a text file specified by the user."""
    path = input("Path: ")
    total = 0
    with open(path, 'r') as f:
        for line in f:
            total += int(line)
    return total

#foo = str(SumFileLines())
#print(foo[0:10])

def ModifyFile():
    """Changes lines in a text file to include 'f# =' because the exercise gives just a big block of numbers...which I only now realize is just fine."""
    f = False
    count = 1
    while True:
        path = input("Open file: ")                
        try:
            with open(path, 'r') as f:
                with open(path+"_new", 'w') as n:
                    for line in f:
                        n.write("f" + str(count) + " = " + line)
                        count += 1
            break
        except IOError:
            decision = input("That file wasn't found.  Type /quit to exit, /y to create a new file with that path, or /n to try again.\n")
            if (decision=="/quit"): 
                try: 
                    f.close()
                except AttributeError:
                    pass #Just want to gracefully handle if the file wasn't found above...probably a better way to do this
                finally:
                    return
            elif(decision=="/y"):
                with open(path, 'wt') as f:
                    f.write("Mooooooo")
                break        

#This exercise produces a chain of integers based on two criteria, looking for a starting number under one million which produces the largest chain

def ChainEval(num):
    """Simply produces the correct output based on the criteria of the problem."""
    if (num <= 1):
        return 1
    elif (num%2 == 0):
         return int(num/2)
    else:
        return int(3*num + 1)

def BuildChain(starting):
    """Builds and returns the chain of numbers given a starting value."""
    isDone = False
    chain = [starting]
    current = starting
    while(isDone != True):
        current = ChainEval(current)
        if(current<=1):
            chain.append(current)
            isDone=True
        else:
            chain.append(current)
    return chain

def FindLongestChain(num):
    """Iterates through all elements under one million that produces the longest chain"""
    longest = []
    lelement = 0
    for element in range(num):
        current = BuildChain(element)
        if(len(current) > len(longest)):
            longest = current
            lelement = element
    print("Longest element is: " + str(lelement) + " with length " + str(len(longest)))
    print(longest)

#FindLongestChain(1000000)

#This exercise attempts to find the total number of paths through a grid that doesn't allow backtracking.  Hard to explain in text.
#However, it appears that you can think of it as a binary decision tree, with a diminishing quantity of 'decisions' to draw from, defined by the dimensions.
#For instance, in a 2x1 (2 rows, 1 column) map has 3 possible decision paths.  The number can be found by making the tree, then counting the leaf nodes.

def BinTree(dimX, dimY, branches):
    """Takes the dimensions of a gride, then attempts to find all non-backtracking paths through it from one corner to the one opposite it."""
    leaves = 0    

    if (dimX<=0 or dimY <=0): #if we run out of one directional stack, we've only got one path we can take from there--the remainder of the other stack
        leaves += 1
    elif(dimX==dimY):
        leaves += 2*BinTree(dimX - 1, dimY, branches)
    else:            
        #First, we want to check if the branch we need has been calculated already, which would save us some time...I think    
        shouldSkip = False
        for entries in branches:
            if((dimX, dimY) in entries):
                leaves += entries[1]
                shouldSkip = True                
        if(shouldSkip == False):
            leaves += BinTree(dimX - 1, dimY, branches)
            leaves += BinTree(dimX, dimY - 1, branches)
            
            branches.append(((dimX, dimY), leaves))          
        
    return leaves

#branches = []
#foo = BinTree(20, 20, branches)
#print(foo)

#This exercise attempts to find the sum of the digits of a particular power of 2.

def SumDigitsPowerTwo(power):
    power = int(math.pow(2, power))
    powString = str(power)
    total = 0

    for x in powString:
        total += int(x)
    return total

#print(SumDigitsPowerTwo(1000))

#This exercise is to find the number of letters it would take to spell out all the words from 1-1000, inclusive, but excluding hyphens.

def GenerateLetterCount():
    """A hard-coded list of the number of letters for each special number case."""
    letters = {}
    letters.update({0: 0}) #Zero...technicaly four, but no one says 'zero'
    letters.update({1: len('one')})
    letters.update({2: len('two')})
    letters.update({3: len('three')})
    letters.update({4: len('four')})
    letters.update({5: len('five')})
    letters.update({6: len('six')})
    letters.update({7: len('seven')})
    letters.update({8: len('eight')})
    letters.update({9: len('nine')})
    letters.update({10: len('ten')})
    letters.update({11: len('eleven')})
    letters.update({12: len('twelve')})

    letters.update({13: len('thirteen')})
    letters.update({14: len('fourteen')})
    letters.update({15: len('fifteen')})
    letters.update({16: len('sixteen')})
    letters.update({17: len('seventeen')})
    letters.update({18: len('eighteen')})
    letters.update({19: len('nineteen')})

    letters.update({20: len('twenty')})
    letters.update({30: len('thirty')})
    letters.update({40: len('forty')})
    letters.update({50: len('fifty')})
    letters.update({60: len('sixty')})
    letters.update({70: len('seventy')})
    letters.update({80: len('eighty')})
    letters.update({90: len('ninety')})

    letters.update({'hundred' : 7})
    letters.update({'thousand': 8})    

    return letters

def Get(val, letKeys):
    """Retrieves the index of a particular input from the list, like a dictionary."""
    count = -1
    for x in letKeys:
        pass

def ParseInputValue(val):
    """This function attempts to parse an input value against a list of values, and outputs a number."""
    lDict = GenerateLetterCount()
    output = 0
    sval = str(val) #Having is a string means I can use slices and indices for parsing.
    length = len(sval) #Tells us how many digits we're dealing with
    
    if(val==1000): 
        output = lDict[1] + lDict['thousand']
        return output

    if(length==3): #Three digits
        output += lDict[int(sval[0])] #leading hundred value
        output += lDict['hundred']
        if(val%100 != 0): #If we need to add 'and'
            output += 3

    if(length>=2): #At least two digits
        if((int(sval[-2:]) > 9) and (int(sval[-2:]) < 21)):
            output += lDict[int(sval[-2:])]
        elif(int(sval[-2:]) > 20): #If it's between 20 and 100
            foo = str(sval[-2] + '0')
            output += lDict[int(foo)]        
            foo = sval[-1]
            output += lDict[int(foo)]
        else: #if it's 1-9
            foo = sval[-1]
            output += lDict[int(foo)]
    else:
        output += lDict[val]
            
    return output
   
def SumLetterCountTo(num):
    """Although this is worded as a general-purpose function, it only goes up to (and including) 1000."""
    total = 0
    for x in range(1, num+1):
        total += ParseInputValue(x)
    return total

#print(SumLetterCountTo(1000))

#This exercise attempts to traverse a binary tree of integers looking for the greatest sum along the path of leaves adjacent to their stems from root to tip.

import csv

def LinesToLists():
    """Builds a list of lists from text file input, comma seperated."""
    input = open('tri.txt', 'r')
    reader = csv.reader(input)
    
    intList = []
    for line in reader:
        lineList = []
        for item in line:
            lineList.append(int(item))        
        intList.append(lineList)

    return intList    
              
def FindSumInTreeAt(ints, sums, line, col):
    """Attempts to find the sum of a paritcular triangle tree list, recursively."""
    left = 0
    right = 0
    base = 0
    
    if(line > len(ints)-1): #if we're seeking beyond the lowest bound of the pyramid
        return 0
    elif(line == len(ints)-1): #if we're at the leaf nodes
        return ints[line][col]
    else: #if we're at any other branch node
        base = ints[line][col] #Get our current node's value
        if(col==0): #If we're along the left edge, we recurse as normal
            left = FindSumInTreeAt(ints, sums, line + 1, col)
        else:
            #This is where we lookup the existing largest sum, because this node should have already been calculated on the left
            left = sums[line+1][col]
        right = FindSumInTreeAt(ints, sums, line + 1, col + 1) #We're always going to find the right child values this way
        
    #sums is a list of the same dimensions as our int pyramid, but stores the highest sum at each point
    if(left > right):
        base += left
    else:
        base += right
    sums[line][col] = base #modify our sums triangle so that we can reference it later

    return base #we want to spit back the value of the greatest path that we've found from this point

#ints = LinesToLists()
#sums = list(ints)
#foo = FindSumInTreeAt(ints, sums, 0, 0)
#print(foo)

#This exercise attempts to find the total number of Sundays in the 20th century that fell on the first of the month, for every month, for every year.

def BuildDaysDict():
    """Builds a dictionary of how many days are in each month."""
    days = {}
    days.update({1: 31}) #January
    days.update({2: 28}) #Feburary, most months
    days.update({3: 31}) #March
    days.update({4: 30}) #April
    days.update({5: 31}) #May
    days.update({6: 30}) #June
    days.update({7: 31}) #July
    days.update({8: 31}) #August
    days.update({9: 30}) #September
    days.update({10: 31}) #October
    days.update({11: 30}) #November
    days.update({12: 31}) #December

    return days

#1 Jan 1900 was a Monday
#So 1 Jan 1901 was a Tuesday--%7 + 1 retuns to the start date, and 365 in 1900
#Need to calculate between 1 Jan 1901 and 31 Dec 2000
def FindNumDayInYear(day, year):
    """Takes as input the day of the week (Sunday is 1) that the year, also input, started on."""
    leap = False
    if(year%4 == 0):
        leap = True
        if(year%100 == 0 and year%400 != 0):
            leap = False

    sundays = 0

    dDict = BuildDaysDict()
    days = 365
    if(leap): days = 366

    dom = 1 #Day of Month tracker
    month = 1 
    dow = day
    doy = 0

    for x in range(1, days+1):
        doy = x
        dsom = dDict[month]
        if(leap==True and month==2):
            dsom = 29

        if((dom-1)%dsom==0 and dom-1 != 0): #If we're at the day after the end of the current month
            dom = 1
            month += 1
            if(month==13):
                month = 1


        if((dow-1)%7==0): #If we're at the day after the last day of the week, we're at the start of next week
            dow = 1            

        if(dow==1 and dom==1):
            sundays += 1
            print(str(year) + ": " + str(month))

#        print("dom: " + str(dom))
#        print("dow: " + str(dow))
#        print("doy: " + str(doy))
#        print("month: " + str(month))
#        print('-----')

        dom += 1
        dow += 1

    return [dow-1, sundays]

def FindSundaysInTwentieth(sYear, eYear, dYear):
    """The calling function for this exercise."""
    sundays = 0
    dow = dYear
    year = sYear
    end = eYear
    for x in range(year, end+1):
        pair = FindNumDayInYear(dow, x)
        dow = pair[0] + 1
        sundays += pair[1]

    print(sundays)

#FindSundaysInTwentieth(1901, 2000, 3)
    

#This exercise finds the sum of the digits of 100!
def FindSumOfBang(n):
    total = math.factorial(n)
    stotal = str(total)
    foo = 0
    for x in stotal:
       foo += int(x)
       
    print(foo)
    return foo 

#FindSumOfBang(100)

#This exercise attempts to find the sume of all amicable numbers under 10000
def GetProperDivisors(num):
    """Gets the proper set of divisors of a number and returns them as a list."""

    divisors = []
    if(num%2==0):
        half = int(num/2)
    else:
        half = (int(num/3))
    for x in range(1, half + 1):
        if(num%x==0):
            divisors.append(x)

    return divisors

def GetAmicableNumbers(limit):
    """Gets the set of all amicable numbers below (inclusive) a particular limit."""
    pairs = []
    divs1 = []
    divs2 = []

    for x in range(1, limit+1):
        divs1 = GetProperDivisors(x)
        #print(str(x) + ": " + str(divs1))
        if(len(divs1) > 1):#filter out 1 and prime numbers
            sum1 = int(math.fsum(divs1))
            divs2 = GetProperDivisors(sum1)
            sum2 = int(math.fsum(divs2))

            if(sum2 == x and sum1 != x):
                pairs.append([x,sum1])
    return pairs

#foo = GetAmicableNumbers(10000) #This doubles up the answers, so I just ran a calculator against unique pairs
#print(foo)

"""This is just to test how map() works and how to access it.
def MapFunc(x):
    return x*2

foo = range(15)
bar = map(MapFunc, foo)
for e in bar:
    print(e)                     
""" #Ghetto block commenting in Python, I guess.

#This exercise takes an external file of names, sorts them alphabetically, then computes a score for each, and sums the total.
def SumOfNames():
    """Takes an external file of names, sorts them alphabetically, then computers a sccore for each and sums the total."""
    fnames = []    
    with open('names.txt', 'r') as fi:       
        for line in fi:
            names = line.split(',')   
            for name in names:
                fnames.append(name.strip("\""))
    fnames.sort()
    total = 0
    pos = 1
    for name in fnames:
        total += ValueOfName(name)*pos
        pos += 1

    return total

def ValueOfName(name):
    """Uses the letter value dictionary to calculate the value of a name."""
    total = 0
    lDict = ValueOfLetters()
    for letter in name:
        total += lDict[letter]

    return total

def ValueOfLetters():
    """Builds and returns a dictionary to associate a letter with a value."""
    values = {}
    values.update({"A" : 1})
    values.update({"B" : 2})
    values.update({"C" : 3})
    values.update({"D" : 4})
    values.update({"E" : 5})
    values.update({"F" : 6})
    values.update({"G" : 7})
    values.update({"H" : 8})
    values.update({"I" : 9})
    values.update({"J" : 10})
    values.update({"K" : 11})
    values.update({"L" : 12})
    values.update({"M" : 13})
    values.update({"N" : 14})
    values.update({"O" : 15})
    values.update({"P" : 16})
    values.update({"Q" : 17})
    values.update({"R" : 18})
    values.update({"S" : 19})
    values.update({"T" : 20})
    values.update({"U" : 21})
    values.update({"V" : 22})
    values.update({"W" : 23})
    values.update({"X" : 24})
    values.update({"Y" : 25})
    values.update({"Z" : 26})

    return values
                        
#print(SumOfNames())

#This exercise attempts to find the sum of all positive integers which cannot be written as the sum of two abundant numbers.
#Abundant numbers are numbers whose proper divisors sum to a total greater than the abundant number.
#Apparently, all integers above 28123 can be written as the sum of two abundant numbers, so that's our upper limit.

def ExportAbundants():
    """Using what we know, this builds and exports a list of abundant numbers between 12 and 28111, inclusive."""
    abundants = []
    for x in range(12, 28112, ): #Don't think any abundants can be odd.
        s = sum(GetProperDivisors(x))
        if(s>x):
            abundants.append(x) 
            if(x%2==1):
                print(x)           
    with open("abundants.txt", "w") as fi:
        for x in abundants:
            fi.write(str(x))
            fi.write("\n")
            
    print("Abundants exported to text.")

def GetAbundants():
    """Reads a file of abundant numbers and returns the data as a list."""
    li = []
    with open("abundants.txt", "r") as fi:
        for line in fi:
            li.append(int(line))
            
    print("Abundants list fetched.")
    return li

def IsOfTwoAbundants(num, abundants):
    """Attempts to find out whether num is the sum of two abundant numbers, passed in by list."""
    isDone = False
    while(isDone == False):
        for x in abundants:            
            if(x > num): #if either of our abundants are larger than the number, we're obviously done.
                print(str(x) + " is greater than " + str(num))
                return False
            diff = num - x
            isDone = diff in abundants
            if(isDone):
                return True

def SumAllNumsNotTwoAbundants():
    """Sums all integers which cannot be written as the sum of two abundant numbers."""
    total = 0
    abundants = GetAbundants()
    for x in range(0, 28124):
        if(not IsOfTwoAbundants(x, abundants)):
            total += x
    return total
#Slow as fuck, there's gotta be some type of optimization I can do, but my brain is fried.
#print(SumAllNumsNotTwoAbundants())

#This execise attempts to find the one-millionth permutation of the numbers from 0-9
def FindNthPermutation(limit):
    """Finds the nth permutation of the numbers 0-9."""
    permutations = []
    snum = ''
    count = 0    

    return permutations

def RecursivePerm(valueList, counterList, limit):
    """Recursively finds a set of permutations using digits 0-9, inclusive."""
    if(len(valueList)==limit):
        string = '' 
        for x in valueList:
            string += str(x)
        counterList[0] = string
        counterList[1] += 1
        if(counterList[1]%10000 == 0):
            print(str(counterList[1]) + ": " + string)                
        
    else:
        for r in range(limit):
            if(not r in valueList):
                current = list(valueList)
                current.append(r)
                RecursivePerm(current, counterList, limit)

#Inelegant, as it doesn't have a working stop condition, which is why I filtered it to only print multiples of 10k...
#RecursivePerm([], ['',0], 10)           

#This exercise attempts to find the first Fibonacci number with an arbitrary digit length.
def GetFibToLength(limit):
    """Generates a list of the Fibonacci numbers until a definied digit-size limit."""
    fib1 = 1
    fib2 = 1
    term = 2
    length = len(str(term))
    count = 3
    while(length<limit):
        fib1 = fib2
        fib2 = term
        term = fib1 + fib2

        length = len(str(term))
        count += 1
        #print(str.format("{0}: O1: {1} O2: {2} T: {3}", count, fib1, fib2, term))
        
    return count
    
#print(GetFibToLength(1000))

#This exercise attempts to find the value d where 1<d<1000 for which 1/d (as a decimal) produces the longest repeating chain of numbers.
def FindDenom(limit):
    """Iterates through a range of denominator values and attempts to return the value producing the longest repeating chain."""
    previousMax = 0
    for x in range(1, 1000, 2): #Division by even numbers isn't very exciting.
        div = 1/x
        
