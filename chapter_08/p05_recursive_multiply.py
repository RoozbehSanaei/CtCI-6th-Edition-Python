# naive implementation

'''
Recursive Multiply: Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
'''

'''
The function  takes three parameters: 'a', 'b', and 'answer'. 
The purpose of this function is to multiply 'a' and 'b' by adding 'a' to 'answer' repeatedly, 'b' times.

Initial Condition Check:
    The function first checks if 'answer' is 0 and both 'a' and 'b' are not 0. If this is the case, it sets 'answer' to the value of 'a'. 
    This step initializes the accumulation of the result.

Base Case for 'a' and 'b':
    The function then checks if either 'a' or 'b' is 1.
        If 'a' is 1, it returns 'answer'. This is because multiplying by 1 returns the other number, and 'answer' has been accumulating this value.
        Similarly, if 'b' is 1, it also returns 'answer' for the same reason.

Recursive Call and Accumulation:
    The function adds the value of 'a' to 'answer', effectively performing a part of the multiplication process.
    It then makes a recursive call to itself with 'a' unchanged, 'b' decreased by 1 (since one instance of 'a' has been added to 'answer'), and the updated 'answer'.

Repeating the Process:
    This recursive process repeats, adding 'a' to 'answer' and decreasing 'b' each time, until 'b' reaches 1.

Final Result:
    Once 'b' is 1, the recursion stops, and 'answer', which now holds the total of 'a' added 'b' times, is returned as the final product.
'''


def multiply(a, b, answer):
    if answer == 0 and a != 0 and b != 0:
        answer = a
    if a == 1:
        return answer

    if b == 1:
        return answer

    answer += a
    return multiply(a, b - 1, answer)


'''
Main Function:
    Purpose: Begins the multiplication process for two numbers.
    Process:
        Determines which number is bigger and which is smaller.
        Calls a helper function with these two numbers.

Recursive Helper Function:
    Purpose: Calculates the product of the two numbers using a recursive approach.
    Process:
        Base Cases:
            If the smaller number is zero, the function returns zero since any number multiplied by zero is zero.
            If the smaller number is one, it returns the bigger number because any number multiplied by one is itself.
        Recursive Steps:
            Divides the smaller number by two to split the multiplication task.
            Calls itself to calculate the product of the halved smaller number and the bigger number, keeping this result.
            If the original smaller number is odd, makes another recursive call with the adjusted smaller number and the bigger number to account for the remainder. If it's even, uses the result from the previous step again.
        Combining Results:
            Adds the results of the two recursive calls to get the total product.

'''


# Solution 1
def min_product(a, b):
    bigger = b if a < b else a  # a < b ? b : a
    smaller = a if a < b else b  # a < b ? a : b
    return min_product_helper(smaller, bigger)


def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger

    # Compute half. If uneven, compute other half. If even, double it
    s = smaller >> 1  # divide by 2
    side1 = min_product(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller - s, bigger)

    return side1 + side2


'''
    Main Function:
        Purpose: Initiates the multiplication of two numbers.
        Process:
            Identifies the larger and smaller of the two numbers.
            Calls a helper function, passing these numbers and an empty memoization dictionary.

    Recursive Helper Function with Memoization:
        Purpose: Recursively calculates the product of the two numbers, using memoization to store and reuse previously calculated results.
        Process:
            Base Cases:
                Returns zero if the smaller number is zero, as multiplying by zero results in zero.
                Returns the larger number if the smaller number is one, since multiplying by one gives the number itself.
            Memoization Check:
                Checks if the current value of the smaller number is already in the memoization dictionary. If it is, returns the stored result to avoid redundant calculations.
            Recursive Steps:
                Divides the smaller number by two to simplify the multiplication task.
                Makes a recursive call to calculate the product of this halved number and the larger number, using the memoization dictionary. This result is stored.
                For an odd smaller number, makes an additional recursive call with the adjusted smaller number to handle the remaining value. For an even number, the previous result is used again.
            Combining Results with Memoization:
                Adds the results of the two recursive calls, stores this sum in the memoization dictionary under the current smaller number, and returns this sum.
'''

# Solution 2
def min_product_2(a, b):
    bigger = b if a < b else a  # a < b ? b : a
    smaller = a if a < b else b  # a < b ? a : b
    return min_product_2_helper(smaller, bigger, {})


def min_product_2_helper(smaller, bigger, memo):
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger

    if smaller in memo:
        return memo[smaller]

    # Compute half. If uneven, compute other half. If even double it
    s = smaller >> 1
    side1 = min_product_2_helper(s, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_2_helper(smaller - s, bigger, memo)
    # sum and cache
    memo[smaller] = side1 + side2
    return memo[smaller]

'''
    Main Function:
        Purpose: Begins the multiplication process for two numbers.
        Process:
            It determines which of the two numbers is larger and which is smaller.
            Initiates a helper function with these two numbers for the recursive multiplication process.

    Recursive Helper Function:
        Purpose: Performs the multiplication using recursion.
        Process:
            Base Cases:
                If the smaller number is zero, the function returns zero, as multiplying by zero results in zero.
                If the smaller number is one, it returns the larger number, as multiplying by one gives the number itself.
            Recursive Calculation:
                The function halves the smaller number to break down the multiplication into a smaller problem.
                It calls itself recursively with this halved number and the larger number, storing the result of this half multiplication.
            Final Combination:
                If the smaller number is even, it doubles the result of the half multiplication (adding it to itself) and returns this as the final product.
                If the smaller number is odd, it adds the larger number to the doubled half product to account for the remainder and returns this sum as the final product.
'''

# Solution 3
def min_product_3(a, b):
    bigger = b if a < b else a  # a < b ? b : a
    smaller = a if a < b else b  # a < b ? a : b
    return min_product_3_helper(smaller, bigger)


def min_product_3_helper(smaller, bigger):
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger
    s = smaller >> 1
    half_prod = min_product_3_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod

    return half_prod + half_prod + bigger


'''

    Converting to Binary:
        The algorithm begins by converting one of the numbers (let's say 'b') into its binary representation. T
        his is done to utilize the binary digits of 'b' in the multiplication process.

    Setting up for the Multiplication:
        A variable is initialized to hold the product of the multiplication. Initially, this is set to zero.

    Iterating Through Binary Digits:
        The algorithm then iterates through each binary digit of the converted number 'b', starting from the least significant bit (the rightmost bit).

    Multiplying using Binary Digits:
        For each bit in the binary representation of 'b', the algorithm checks if the bit is 1.
        If the bit is 1, it performs a partial multiplication by shifting the other number 'a' to the left by the current bit's position 
        (i.e., multiplying 'a' by 2 raised to the power of the bit's position). 
        This left shift is equivalent to multiplying 'a' by 2 for each position the bit has moved from the rightmost end.
        This partial product is then added to the running total of the product.

    Final Product:
        After iterating through all the bits of 'b', the accumulated sum represents the final product of 'a' and 'b'.

'''



def multiply_bit_based(a, b):
    b_bin = bin(b)
    b_bin = b_bin[2:]
    prod = 0
  
    for i in range(len(b_bin)):  
        if int(b_bin[-i - 1]):
            prod = prod + (a << i)
  
    return prod



test_cases = [(5, 6), (28, 89), (1234, 245334)]
testable_functions = [multiply_bit_based, min_product, min_product_2, min_product_3]


def test_min_product():
    for min_prod in testable_functions:
        for a, b in test_cases:
            assert min_prod(a, b) == a * b


if __name__ == "__main__":
    test_min_product()
