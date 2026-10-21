import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    # variable values
    a = 1
    a_list = [] # make list to place a values in
    a_list.append(a) # place first a value in a list

    b = 1/(math.sqrt(2))
    b_list = [] # list for b values
    b_list.append(b) # place zero b value in b list

    t = 1/4
    t_list = [] # list for t values
    t_list.append(t) # place zero t value in t list

    p = 1
    p_list = [] # list for p values
    p_list.append(p) # place zero p value in p list

    # perform 10 iterations of this loop
    for i in range(0, 10):

        #find the first set of new values where n = 0
        a_1 = (a_list[i] + b_list[i])/2
        a_list.append(a_1)                  # place value in a list
        b_1 = math.sqrt(a_list[i] * b_list[i])
        b_list.append(b_1)                  # place value in b list
        p_1 = 2*(p_list[i])
        p_list.append(p_1)                  # place value in p list
        t_1 = t_list[i] - p_list[i]*((a_1 - a_list[i])**2) 
        t_list.append(t_1)                  # place value in t list
        continue

    pi = ((a_list[10] + b_list[10])**2)/(4*(t_list[10]))
 
    # change this so an actual value is returned    
    return pi


desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)
print("Error within function is:", error)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
