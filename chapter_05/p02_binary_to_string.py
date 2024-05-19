
'''Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR:''''


'''
    Initialize the Binary String: 
        Start with a string that has a decimal point. This string will be used to build the binary representation.

    Validate the Number: 
        Check if the number is within the valid range, which is strictly between 0 and 1 (exclusive). 
        If the number is not in this range, check against a list of edge cases (like "1", "0", "1.0" followed by up to 32 zeros, etc.). 
        If the number does not fall within these acceptable values, return an error message.

    Convert to Binary:
        Repeat the following steps as long as the number is greater than 0:
            If the binary string exceeds 32 characters, stop and return the current string.
            Multiply the number by 2.
            If the result is 1 or greater, add "1" to the binary string and subtract 1 from the number.
            If the result is less than 1, add "0" to the binary string.
        This process essentially shifts the number's decimal point to the right, determining each bit of the binary fraction.

    Complete the Binary String: 
        If the binary string is shorter than 33 characters, pad it with zeros until it reaches this length. 
        This ensures a consistent length for the binary representation.

    Return the Binary String: 
        Finally, return the binary string representing the fractional part of the original number.

'''

def bin_to_string(number):
    bit_str = "."

    if number >= 1.0 or number <= 0.0:
        good_nums = ["1"] + ["1.0" + "0" * i for i in range(32)]
        good_nums += ["0"] + ["0.0" + "0" * i for i in range(32)]
        if str(number) not in good_nums:
            return "ERROR"

    while number > 0:
        if len(bit_str) > 32:
            return bit_str

        two = number * 2

        if two >= 1:
            bit_str += "1"
            number = two - 1
        else:
            bit_str += "0"
            number = two

    return bit_str.ljust(33, "0")



'''
    Scale the Number: 
        Multiply the fractional number by 2^32. 
        This scaling transforms the fractional part into an integer, which is easier to convert into binary. 
        It effectively shifts the fractional part to the left of the decimal point, preparing it for binary conversion.

    Error Handling for Overflow: 
        Check if the scaled number exceeds the maximum value for a 32-bit representation (2^32). 
        If it does, return an error message, as the number cannot be accurately represented within 32 bits.

    Adjust for Exact 32-bit Limit: 
        If the scaled number equals 2^32, decrement it by 1. 
        This adjustment ensures that the number fits within the 32-bit limit.

    Binary Conversion: 
        Initialize an empty string to hold the binary representation.
        Perform a loop for 32 iterations, corresponding to the 32 bits of precision.
        In each iteration, extract the least significant bit (LSB) of the current number by taking the modulo 2 of the number. Prepend this bit to the binary string.
        Then, perform a floor division by 2 on the number to prepare for the next iteration. 

    Finalize the Binary Representation: 
        Prepend a decimal point to the binary string. 
        This indicates that the binary string represents the fractional part of the original number.

    Return the Result: 
        The final string, which is the binary representation of the fractional part of the input number, is returned.

'''


def bin_to_string_alt(number):
    number_s31 = int(number * (2**32))

    if number_s31 > 2**32:
        return "ERROR"

    if number_s31 == (2**32):
        number_s31 = 2**32 - 1

    ans = ""

    for _ in range(32):
        ans = str(number_s31 % 2) + ans
        number_s31 = number_s31 // 2

    return "." + ans


def example():
    for number in [0.625, 0, 0.1, 0.101, 0.2, 0.5, 1, 2]:
        bit_str = bin_to_string(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Number: {number}, Binary String: {response}")
        bit_str = bin_to_string_alt(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Number: {number}, Binary String: {response}")
        assert bin_to_string(number) == bin_to_string_alt(number)


if __name__ == "__main__":
    example()
