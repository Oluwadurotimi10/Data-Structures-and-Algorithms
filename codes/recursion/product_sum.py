# A function that takes in a special array and returns uts product sum.
# E.g product sum of [x, [y,z,[s]]] is x + 2 * (y + z + 3 *(s))

def productSum(array):
    # Write your code here.
    def main(array, level=1):
        product_sum = 0
        for val in array:
            if type(val) is list:
                product_sum += level * main(val, level + 1)
            else:
                product_sum += val * level
        return product_sum

    return main(array)
