"""ENGR 315 | Nonlinear Systems Assignment

Complete the four functions below. Do not change their names, parameters,
or return types. Submit this file to Gradescope.

You may use NumPy and SciPy. Do not hard-code the final dimensions.
"""
import numpy as np
from scipy.optimize import root


def residuals(dimensions):
    """Return a NumPy array of shape (2,) with [f1, f2].

    f1(x, y) = x**2 + y**2 - 41
    f2(x, y) = x + y - 9
    """
    # TODO (20 points): implement the nonlinear equations.
    x, y = dimensions
    return np.array([x**2 + y**2 - 41, x+y-9], dtype=float)


def jacobian(dimensions):
    """Return a NumPy array of shape (2, 2) containing the Jacobian."""
    # TODO (20 points): implement the Jacobian matrix.
    x, y = dimensions
    return np.array([[2*x, 2*y], [1.0, 1.0]], dtype=float)


def newton_raphson(initial_guess, tolerance=1e-6, max_iterations=50):
    """Return a NumPy array of shape (2,) with the converged dimensions.

    Use a for loop and np.linalg.solve(J, -F). Stop when the maximum
    absolute residual is strictly smaller than tolerance. If the solver
    does not converge within max_iterations, raise RuntimeError.
    """
    # TODO (40 points): implement the iterative Newton-Raphson algorithm.
    dimensions = np.array(initial_guess, dtype=float)
    
    for iteration in range(max_iterations + 1):
            residual = residuals(dimensions)
            error = np.max(np.abs(residual))
    
            if error < tolerance:
                return dimensions, True
    
            if iteration == max_iterations:
                break
    
            # J * correction = -F : reuse np.linalg.solve from linear systems!
            jacobia = jacobian(dimensions)
            try:
                correction = np.linalg.solve(jacobia, -residual)
            except np.linalg.LinAlgError as exc:
                raise ValueError(
                    "Newton-Raphson cannot proceed: the Jacobian is singular. "
                    "Try a different initial guess."
                ) from exc
    
            dimensions = dimensions + correction
    
    return dimensions, False


def solve_scipy(initial_guess):
    """Return a NumPy array of shape (2,) using scipy.optimize.root.

    Check solution.success. Raise RuntimeError if the solver fails.
    """
    # TODO (20 points): use root() to solve the system.
    #need a function and an inital guess. could add a method for solving but not necessary (default is powell hybrid)

    def equation(dimensions):
        x, y = dimensions
        f1 = x**2 + y**2 - 41
        f2 = x + y - 9
        return [f1, f2]
    initial_guess = [2,4]
    solution = root(equation, initial_guess)

    return solution

if __name__ == "__main__":
    guess = np.array([3.0, 6.0])
    print("Initial guess:", guess)
    print("Residuals at guess:", residuals(guess))
    print("Jacobian at guess:\n", jacobian(guess))
    print("NumPy Newton-Raphson:", newton_raphson(guess))
    print("SciPy root:", solve_scipy(guess))
