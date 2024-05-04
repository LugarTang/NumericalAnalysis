import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_n(app, real):
    err = abs(app - real)
    m = 0
    while(app >= 1):
        app = app/10
        m += 1
    return math.floor(math.log10(0.5/err) + m)

def relative_error(app, real):
    return abs(app - real) / abs(app)

def taylor_approximation(x, n):
    result = 0
    for i in range(n+1):
        result += (-1)**i * x**i / math.factorial(i)
    return result

def taylor_approximation_iterative(x, n):
    a_n = 1  # a_0 = 1
    result = a_n
    for i in range(1, n+1):
        a_n = -a_n * x / i
        result += a_n
    return result

def taylor_approximation_iterative_rec(x, n):
    a_n = 1  # a_0 = 1
    result = a_n
    for i in range(1, n+1):
        a_n = a_n * x / i
        result += a_n
    return 1/result  # take the reciprocal to get e^-x

if __name__ == "__main__":
    for i in range(1, 9):
        print("n = ", i)
        xs = []
        reals = []
        app1s = []
        app2s = []
        app3s = []
        for x in np.arange(0, 101, 10):
            xs.append(x)
            reals.append(math.exp(-x))
            app1s.append(taylor_approximation(x, i)-math.exp(-x))
            app2s.append(taylor_approximation_iterative(x, i)-math.exp(-x))
            app3s.append(taylor_approximation_iterative_rec(x, i)-math.exp(-x))
        # for each approximation, calculate mean squared error
            


        plt.plot(xs, app1s, label='Approximation 1')
        plt.plot(xs, app2s, label='Approximation 2')
        plt.plot(xs, app3s, label='Approximation 3')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
    # real = math.sqrt(30)
    # approx = 5.5
    # print("n = ", calculate_n(approx, real))
    # print("Relative error: ", relative_error(approx, real))

