import numpy as np
from cal_num import relative_error 
import math

class sample_point:
    def __init__(self, x, ys):
        self.x = x
        self.ys = ys # This contains f(x), f'(x), f''(x), ...

def divided_difference(sample_points):
    n = len(sample_points)
    if n == 1:
        return sample_points[0].ys[0]
    elif all([sample_points[i].x == sample_points[0].x for i in range(n)]): # check whether all same x value - return derivative
            return sample_points[0].ys[n-1]/math.factorial(n-1)
    else:
        return (divided_difference(sample_points[1:]) - divided_difference(sample_points[:-1]))/(sample_points[n-1].x-sample_points[0].x)

def sample_at_divided_interval(start, end, n, f):
    sample_points = []
    for i in range(n+1):
        x = start + i*(end-start)/n
        sample_points.append(sample_point(x, [f(x)]))
    return sample_points

def lagrange(sample_points):
    xs = [sample_point.x for sample_point in sample_points]
    ys = [sample_point.ys[0] for sample_point in sample_points]
    # print(xs,ys)
    base_functions = []
    for i in range(len(xs)):
        base_functions.append(lambda x, i=i: np.prod([(x-xs[j])/(xs[i]-xs[j]) for j in range(len(xs)) if j != i]))
    return lambda x: sum([ys[i]*base_functions[i](x) for i in range(len(xs))])

f = lambda x: 1/(1+x**2)
start = -5
end = 5
n = 10
sample_points = sample_at_divided_interval(start, end, n, f)
# In each interval calculate the error between f((start+end)/2) and (f(start) + f(end)) / 2

real_values = []
apprx_values = []
for i in range(n):
    interval_start = sample_points[i].x
    interval_end = sample_points[i+1].x
    interval_mid = (interval_start + interval_end) / 2
    interval_avg = (sample_points[i].ys[0] + sample_points[i+1].ys[0]) / 2

    real_values.append(f(interval_mid))
    apprx_values.append(interval_avg)

print("Real values: ", real_values)
print("Approximation values: ", apprx_values)