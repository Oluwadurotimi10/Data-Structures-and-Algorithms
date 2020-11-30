def power(base,exp):
    assert exp >= 0 and int(exp) == exp; "Ensure the exp is a whole number and positive"
    if exp == 0:
        return 1
    return base * power(base,exp-1)

print(power(4,3))