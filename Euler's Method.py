import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t0, tn, h):
    """
    Approximate the solution of the ODE y' = f(t, y) using Euler's method.

    Parameters:
        f: The function representing the right-hand side of the ODE.
        y0: The initial value of the dependent variable.
        t0: The initial value of the independent variable.
        tn: The final value of the independent variable.
        h: The step size.

    Returns:
        t_values: Array of time values.
        y_values: Array of approximate solutions.
    """
    t_values = np.arange(t0, tn + h, h)
    y_values = [y0]

    for t in t_values[:-1]:
        y0 = y0 + h * f(t, y0)
        y_values.append(y0)

    return t_values, y_values

# Example: Solving y' = -y, y(0) = 1
def my_function(t, y):
    return -y

# Initial values
initial_t = 0
final_t = 5
initial_y = 1
step_size = 0.1

# Applying Euler's method
t_values, y_values = euler_method(my_function, initial_y, initial_t, final_t, step_size)

# Plotting the results
plt.plot(t_values, y_values, label="Euler's Method")
plt.title("Euler's Method for y' = -y")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.show()
