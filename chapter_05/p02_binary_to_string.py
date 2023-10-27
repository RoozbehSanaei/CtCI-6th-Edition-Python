
'''Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR:''''

def bin_to_string(number):
    # Initialize the string to store the binary representation
    # Always starts with a decimal point
    bit_str = "."
    
    # Check if the number is outside the allowed range (0, 1)
    # or is not exactly 0 or 1
    if number >= 1.0 or number <= 0.0:
        good_nums = ["1"] + ["1.0" + "0" * i for i in range(32)]
        good_nums += ["0"] + ["0.0" + "0" * i for i in range(32)]
        if str(number) not in good_nums:
            return "ERROR"

    # Loop to calculate binary representation
    while number > 0:
        # If the binary string becomes too long, exit
        if len(bit_str) > 32:
            return bit_str
        
        # Multiply the fractional part by 2
        two = number * 2
        
        # Check if the resulting number has a whole part of 1
        if two >= 1:
            bit_str += "1"  # Append "1" to the binary string
            number = two - 1  # Remove the whole part
        else:
            bit_str += "0"  # Append "0" to the binary string
            number = two  # Keep the fractional part

    # If the binary string is shorter than 33 characters,
    # pad it with zeros on the right
    return bit_str.ljust(33, "0")


def bin_to_string_alt(number):
    # Scale the number by 2**32 to work with integers
    number_s31 = int(number * (2**32))
    
    # Check if the scaled number exceeds the 32-bit limit
    if number_s31 > 2**32:
        return "ERROR"

    # If the scaled number equals 2**32, decrement it by 1
    # to fit within 32 bits
    if number_s31 == (2**32):
        number_s31 = 2**32 - 1

    # Initialize an empty string to store the binary representation
    ans = ""
    
    # Loop through 32 iterations to convert the number to binary
    for _ in range(32):
        # Append the least significant bit to the left of 'ans'
        ans = str(number_s31 % 2) + ans
        # Floor divide the number by 2 for the next iteration
        number_s31 = number_s31 // 2

    # Add a decimal point at the beginning and return
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
