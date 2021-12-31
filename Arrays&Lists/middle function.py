def middle(lst):
    """
        This function takes in a list and returns a list that contains all but 
        the first and last elements.
    """
    new = []
    stop = len(lst)-1
    for i in range(1,stop):
        new.append(lst[i])
    return new
mylist = [3,7,9,3,67,9]
print(middle(mylist))