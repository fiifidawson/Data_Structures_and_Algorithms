def mark_inventory(clothing_items):
    clothing_options = []
    for item in clothing_items:
    # For sizes 1 through 5 (Python ranges go UP TO second
    # number, but do not include it):
        for size in range(1, 6):
            clothing_options.append(item + " Size: " + str(size))
    return clothing_options

#Chapter 7
# Time complexity: Is not O(n^2) because nested loops depend N for both loops.
# The range for the inner loop for this algorithm is constant