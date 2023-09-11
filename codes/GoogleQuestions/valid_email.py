# Leetcode 929

# TC O(N.M)

"""
    Time Complexity: O(N.M)
In the worst case, we iterate over all the characters of each of the emails given.
If we have N emails and each email has M characters in it. Then complexity is of order (Number of emails) * (Number of characters in average email) = N*M.

Space Complexity: O(N.M)
In the worst case, when all emails are unique, we will store every email address given to us in the hash set.
"""
def numUniqueEmails(self, emails: List[str]) -> int:
    count = 0
    distinct = set()
    for mail in emails:
        temp = mail.split('@')
        local_name = temp[0].split('+')[0].replace('.', '')
        valid = local_name + '@' + temp[1]
        print(valid)
        if valid not in distinct:
            distinct.add(valid)
    return len(distinct)