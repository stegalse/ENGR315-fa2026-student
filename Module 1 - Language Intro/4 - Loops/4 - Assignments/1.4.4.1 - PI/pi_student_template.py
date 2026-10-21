import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1/(math.sqrt(2))
t = 1/4
p = 1

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    #find the first set of new values where n = 0
    a_1 = (a + b)/2
    b_1 = math.sqrt(a * b)
    p_1 = 2*p
    t_1 = t - p*((a_1 - a)**2)

    pi_1 = ((a_1 + b_1)**2)/(4*t_1)

    #find the next 9 values
    a_i = (a_1 + b_1)/2
    b_i = math.sqrt(a_1 * b_1)
    p_i = 2*p_1
    t_i = t_1 - p_1*((a_i - a_1)**2)
    pi_i = ((a_i + b_i)**2)/(4*t_i)
    continue 


    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = pi_i

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
