# my name is Ortal Dayan
# my phone number is : 053-4205134

def friendly_bytes(number_of_bytes, decimals=2, binary=False):
    if number_of_bytes < 0:
        return
    units = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'] # array of units, I start the array with an empty string, because if the output is the smallest unit, it will only receive the suffix B or iB
    if binary: # In this condition I determine the base according to the binary parameter
        base = 1024
        base_char = 'iB'
    else:
        base = 1000
        base_char = 'B'
    for unit in units:  #In this loop I go through the units, take the number and each time divide it by the base (1000 or 1024),
        # each additional division actually indicates a larger number and therefore we will also get a larger unit (according to its position in the loop)
        if number_of_bytes < base:
            return str(round(number_of_bytes, decimals)) + " " + unit + base_char
        number_of_bytes /= base


# You can test the function by the test.py file or through here by the print function
print(friendly_bytes(102))
print(friendly_bytes(1111111111, binary=True))
