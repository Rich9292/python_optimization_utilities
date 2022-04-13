from scipy.optimize import minimize
# used: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize

# initial guess
x0 = [0,0]

# bounds for args to optimize
bounds = ((-4,4),(-3,3))

# extra static args to pass in
args = ('arg_1','arg_2')

# function to minimize
def f(x, *params):
    print(params[0])
    print(params[1])
    z = x[0] + x[1]
    return -z

# run optimizer
res = minimize(f, x0, bounds = bounds, args = args, method='Nelder-Mead', tol=1e-6)


print(res.success)
print("Argument values are: ",res.x)
print("Resulting function value is: ",res.fun)
