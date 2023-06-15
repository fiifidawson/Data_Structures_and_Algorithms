### Chapter 12 [1/May/2023]

## Dynamic Programming
Dynamic programming takes the flaws associated with recusrion or programming in general in terms on efficiency and 
makes it better. Instead of initializing a new process to a similar old process, the results of the process is stored in a variable to be use later by the function.
code—the
mere storing of a computation in a variable—ended up changing the speed of our function from O(2^N) to O(N).

When a problem is solved by solving smaller versions of the same problem, the smaller problem is called a subproblem.


## Using Memoization
Example
Bad Recursion:
 def fibonacci(n)
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 2) + fibonacci(n -1)

Good Recursion
def fib(n, memo):
    if n == 0 or n == 1:
        return n
    
    # Check the hash table (called memo) to see whether fib(n)
    # was already computed or not:
    
    if not memo.get(n):
    # If n is NOT in memo, compute fib(n) with recursion
    # and then store the result in the hash table:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    # By now, fib(n)'s result is certainly in memo. (Perhaps
    # it was there before, or perhaps we just stored it there
    # in the previous line of code. But it's certainly there now.)
    # So let's return it:
    return memo[n]

## Using 'Going Bottom Up'
def fib(n):
    if n == 0:
        return 0
    # a and b start with the first two numbers in the
    # series, respectively:
    a = 0
    b = 1
    # Loop from 1 until n:
    for i in range(1, n):
    # a and b each move up to the next numbers in the series.
    # Namely, b becomes the sum of b + a, and a becomes what b used to be.
    # We utilize a temporary variable to make these changes:
        temp = a
        a = b
        b = temp + a
    return b