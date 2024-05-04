import numpy as np
import matplotlib.pyplot as plt

def least_square(x,y,base_functions,print_matrix=False):
    n = len(x)
    m = len(base_functions)
    A = np.zeros((m,m))
    B = np.zeros(m)
    for i in range(m):
        for j in range(m):
            A[i][j] = sum([base_functions[i](x[k])*base_functions[j](x[k]) for k in range(n)])
        B[i] = sum([y[k]*base_functions[i](x[k]) for k in range(n)])
    if print_matrix:
        print(A)
        print(B)
    return np.linalg.solve(A,B)

if __name__ == "__main__":
    x=[19,25,31,38,44]
    y=[19.0,32.3,49.0,73.3,97.8]
    base_functions = [lambda x: 1, lambda x: x*x]
    a,b = least_square(x,y,base_functions, True)
    print(a,b)
    bx2 = [b*sample*sample for sample in x]
    print("MSE: ", np.sum([(y[i] - a - bx2[i])**2 for i in range(len(x))]))
    # plot the sample points 
    plt.plot(x,y,'ro')
    # plot the approximation function in a more detailed way
    x_draw = np.linspace(0,50,100)
    y_draw = [a + b*sample*sample for sample in x_draw]
    plt.plot(x_draw,y_draw)
    plt.show()

    # print("Real values: ", real_values)
    # print("Approximation values: ", apprx_values)
    # print("Error: ", relative_error(real_values, apprx_values))