# ===============================================================
#Recursion = a function calling itself to solve a smaller version of the same problem.

#You want to solve a big problem (say, count down from 10).
#Instead of solving it all at once, you say:
#“I’ll print 10 now, and let future me print the rest.”
#Each future me does one step, until someone finally says: “Stop, we’re done.”
#That “stop point” is the base case.

#Structure of a Recursive Function
# ----------------------------------------------------------------
#Every recursive function has two essential parts:
#Base Case → The condition where the function stops calling itself.
#Without this, recursion goes on forever (infinite loop → stack overflow).
#Example:

#if n == 0:
#    return 1

#Recursive Case → The part where the function calls itself again with a smaller/simpler input.
#Example:

#return n * factorial(n-1)

# ===================== Countdown Algorithm =====================

def countdown(n):
    if n == 0:  # base case
        print("Blastoff!")
    else:       # recursive case
        print(n)
        countdown(n-1)
print(" ---------------- Countdown Algorithm ----------------")
countdown(3)

# =================================================================

# ====================== Factorial Algorithm ======================

def Factorial(n):
    if n == 0: return 1
    else:
        return n * Factorial(n-1)

print(Factorial(5))

# =================================================================

# ====================== Fibonacci Algorithm ======================

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))

# =================================================================
