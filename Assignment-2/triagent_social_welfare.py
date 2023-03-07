import cvxpy as cp

# Define the variables
p_01 = cp.Variable(1, nonneg=True)
p_02 = cp.Variable(1, nonneg=True)
p_03 = cp.Variable(1, nonneg=True)
p_04 = cp.Variable(1, nonneg=True)

p_11 = cp.Variable(1, nonneg=True)
p_12 = cp.Variable(1, nonneg=True)
p_13 = cp.Variable(1, nonneg=True)
p_14 = cp.Variable(1, nonneg=True)

p_21 = cp.Variable(1, nonneg=True)
p_22 = cp.Variable(1, nonneg=True)
p_23 = cp.Variable(1, nonneg=True)
p_24 = cp.Variable(1, nonneg=True)

# find a correlated equilibrium maximizing social welfare

obj = cp.Maximize(3 * p_01 + p_03 + 6 * p_11 + 6 * p_14 + p_23 + 3*p_24)

constraints = [p_01 + p_02 + p_03 + p_04 + p_11 + p_12 + p_13 +
               p_14 + p_21 + p_22 + p_23 + p_24 == 1]  # probabilities sum to 1

# row player has no incentive to deviate
constraints += [2*p_11 + p_03 + 2*p_14 >= p_01 + 2*p_13 + 2*p_12]


# column player has no incentive to deviate
constraints += [2*p_11+p_23 + 2 * p_14 >= 2*p_13 + 2*p_12 + p_24]

# matrix player has no incentive to deviate
constraints += [3*p_01 + 2*p_11+2*p_14 + 3*p_24 >=
                2*p_01+3*p_04+3*p_11+3*p_14+3*p_21+2*p_24]


prob = cp.Problem(obj, constraints)

prob.solve()


print("The optimal value is", prob.value)
print("The value of p_01 is", p_01.value)
print("The value of p_02 is", p_02.value)
print("The value of p_03 is", p_03.value)
print("The value of p_04 is", p_04.value)
print("The value of p_11 is", p_11.value)
print("The value of p_12 is", p_12.value)
print("The value of p_13 is", p_13.value)
print("The value of p_14 is", p_14.value)
print("The value of p_21 is", p_21.value)
print("The value of p_22 is", p_22.value)
print("The value of p_23 is", p_23.value)
print("The value of p_24 is", p_24.value)
