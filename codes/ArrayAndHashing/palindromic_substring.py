def funcSubstring(inputStr):
    # Write your code here
    pal_substrings = ['']
    str_length = len(inputStr)

    for s in range(str_length):
        # checking for odd length palindrome
        left_ptr = s
        right_ptr = s

        while left_ptr >= 0 and right_ptr < str_length and inputStr[left_ptr] == inputStr[right_ptr]:
            left_ptr -= 1
            right_ptr += 1
        curr_palindrome = inputStr[left_ptr + 1:right_ptr]
        if len(curr_palindrome) != 1 and curr_palindrome != '':
            if len(curr_palindrome) > len(pal_substrings[0]):
                pal_substrings[0] = curr_palindrome
            elif len(curr_palindrome) == len(pal_substrings[0]):
                pal_substrings[0] = min(pal_substrings[0], curr_palindrome)

        # checking for even length palindrome
        left_ptr = s
        right_ptr = s + 1
        while left_ptr >= 0 and right_ptr < str_length and inputStr[left_ptr] == inputStr[right_ptr]:
            left_ptr -= 1
            right_ptr += 1
        curr_palindrome = inputStr[left_ptr + 1:right_ptr]
        if len(curr_palindrome) != 1 and curr_palindrome != '':
            if len(curr_palindrome) > len(pal_substrings[0]):
                pal_substrings[0] = curr_palindrome
            elif len(curr_palindrome) == len(pal_substrings[0]):
                pal_substrings[0] = min(pal_substrings[0], curr_palindrome)

    # print(pal_substrings)
    if pal_substrings[0] == '':
        return None

    return pal_substrings[0]
