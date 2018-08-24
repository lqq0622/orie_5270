import numpy as np
from scipy import optimize
import random


def rosenbrock(x):
    """
    x: an array with len 3 (a data point on function)
    output: return the rosenbrock function value (n = 3)
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    return (100.0 * ((x2 - x1 ** 2.0) ** 2.0) + (1.0 - x1) ** 2.0 + 100.0 * ((x3 - x2 ** 2.0) ** 2.0) + (
            1.0 - x2) ** 2.0)


def rosen_grad(x):
    """
    x: an array with len 3 (a data point on function)
    output: return the rosenbrock gradient for x
    """
    # n = 3
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    grad = np.array([0.0, 0.0, 0.0])
    grad[0] = -400.0 * x1 * (x2 - x1 ** 2.0) - 2.0 * (1.0 - x1)
    grad[1] = 200.0 * (x2 - x1 ** 2.0) - 400.0 * x2 * (x3 - x2 ** 2.0) - 2.0 * (1.0 - x2)
    grad[2] = 200.0 * (x3 - x2 ** 2.0)

    return grad


def get_rosen_min(iteration):
    global_min = np.inf
    min_x = np.array([])

    for i in range(iteration):
        x0 = np.array([float(num) for num in random.sample(range(-50, 50), 3)])
        result = optimize.minimize(rosenbrock, x0=x0, jac=rosen_grad, method='BFGS')

        if result.fun < global_min:
            global_min = result.fun
            min_x = result.x

    print("rosenbrock(n=3) has minimum value", global_min, "when x =", min_x)


if __name__ == "__main__":
    get_rosen_min(25)

