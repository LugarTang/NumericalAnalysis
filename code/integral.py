import math 

def composite_trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s

def composite_simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 4 * f(a + i * h - 0.5 * h)
        s += 2 * f(a + i * h)
    s += 4 * f(a + n * h - 0.5 * h)
    return h / 6 * s

if __name__ == "__main__":
    # f = lambda x: x / (4 + x**2)
    # a = 0
    # b = 1
    # n = 8
    # print("Composite Trapezoidal: ", composite_trapezoidal(f, a, b, n))
    # print("Composite Simpson: ", composite_simpson(f, a, b, n))
    f = lambda x: math.exp(x)
    a = 0
    b = 1
    n = 3
    true_value = math.exp(1) - 1
    # print("Composite Trapezoidal: ", composite_trapezoidal(f, a, b, n))
    # print("Error: ", true_value - composite_trapezoidal(f, a, b, n))
    print("Composite Simpson: ", composite_simpson(f, a, b, n))
    print("Error: ", true_value - composite_simpson(f, a, b, n))