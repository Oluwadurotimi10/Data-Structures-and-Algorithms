# Leetcode 299

def getHint(self, secret: str, guess: str) -> str:
    bulls = 0
    cows = 0
    nums = [0] * 10

    for i, j in enumerate(secret):
        s = int(secret[i])
        g = int(guess[i])

        if s == g:
            bulls += 1
        else:
            # this value has been seen in the guess before
            if nums[s] < 0:
                cows += 1
            # this value has been seen in the secret before
            if nums[g] > 0:
                cows += 1
            nums[s] += 1
            nums[g] -= 1
    return str(bulls) + 'A' + str(cows) + 'B'

# using counter
def getHint(self, secret: str, guess: str) -> str:
    secret = list(secret)
    guess = list(guess)
    bulls = 0
    cows = 0
    count_map = collections.Counter(secret)
    print(count_map)

    for k in range(len(guess)):
        if guess[k] == secret[k]:
            bulls += 1
            count_map[secret[k]] -= 1
            guess[k] = 'A'
            secret[k] = 'A'
    for k in range(len(guess)):
        if guess[k] != 'A' and count_map[guess[k]] > 0:
            cows += 1
            count_map[guess[k]] -= 1
            guess[k] = 'B'

    return str(bulls) + 'A' + str(cows) + 'B'


# similar google interview question
"""
secret = [B,G,Y,G]                        
guess =  [B,R,G,G]
"""

#using the first method
def find_black_white_pairs(self, secret: str, guess: str):
    black = 0
    white = 0
    alphas = [0] * 26

    for i in range(len(guess)):
        idxG = ord(guess[i]) - ord('A')
        idxS = ord(secret[i]) - ord('A')

        if guess[i] == secret[i]:
            black += 1
        else:
            #the color has appeared before in guess
            if alphas[idxS] < 0:
                white += 1
            # the color has appeared before in secret
            if alphas[idxG] > 0:
                white += 1
            alphas[idxS] += 1
            alphas[idxG] -= 1
    return [black, white]


# using counter
def find_black_white_pairs(self, secret: str, guess: str):
    black = 0
    white = 0
    count = collections.Counter(secret)

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            black += 1
            count[secret[i]] -= 1
            secret[i] = 1
            guess[i] = 1

    for i in range(len(guess)):
        if guess[i] != 1 and count[guess[i]] > 0:
            white += 1
            count[guess[i]] -= 1
            guess[i] = 2
    return [black, white]



