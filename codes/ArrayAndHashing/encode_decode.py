
"""
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
    decoded back to the original list of strings.

    Please implement encode and decode
"""

def encode(self, strs):
    # write your code here
    code = ""
    for s in strs:
        code += str(len(s)) + "#" + s
    return code

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""

def decode(self, str):
    # write your code here
    output = []
    i = 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        decoded = str[j + 1:length + j + 1]
        output.append(decoded)
        i = length + j + 1
    return output
