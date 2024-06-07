import numpy as np
from scipy.optimize import minimize


def objective_function(x):
    return 25000*x[0] + 25000*x[1] + 150000*x[2] + 100000*x[3] + 25000*x[4] + 50000*x[5] + 25000*x[6] + 150000*x[7] + 60000*x[8] + 25000*x[9] 

def constraint1(x):
    return 120 - (15*x[0] + 15*x[1] + 15*x[2] + 15*x[3] + 15*x[4] + 15*x[5] + 8*x[6] + 10*x[7] + 15*x[8] + 15*x[9])

def constraint2(x):
    return 100 - (5*x[0] + 5*x[1] + 30*x[2] + 20*x[3] + 5*x[4] + 10*x[5] + 5*x[6] + 30*x[7] + 12*x[8] + 5*x[9])


bounds = [(0, 1)] *10


constraints = ({'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2})


x0 = np.random.rand(10)


result = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=constraints)

solusi_optimal = np.round(result.x)

print('Solusi optimal:', solusi_optimal)
print('Z:', int(result.fun))