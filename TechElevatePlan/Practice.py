def add_until_100(array):
    if len(array) == 0:
        return 0
    else:
        sum_rest = add_until_100(array[1:])
        if array[0] + sum_rest > 100:
            return sum_rest
        else:
            return array[0] + sum_rest
