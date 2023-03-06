import cvxpy as cp
import numpy as np


edge_AD = cp.Variable(1, integer=True)
edge_AB = cp.Variable(1, integer=True)
edge_AC = cp.Variable(1, integer=True)
edge_DB = cp.Variable(1, integer=True)
edge_BC = cp.Variable(1, integer=True)
edge_BE = cp.Variable(1, integer=True)
edge_CE = cp.Variable(1, integer=True)

constraints = [edge_AD + edge_AB + edge_AC == -2,
               edge_DB - edge_AB == 7,
               - edge_DB - edge_AB + edge_BC == -2,
               -edge_AC - edge_BC + edge_CE == 3,
               -edge_BE - edge_CE == -6]

maximize = cp.Minimize(3 * cp.abs(edge_AD) + 6 * cp.abs(edge_AB) + 4 * cp.abs(edge_AC)
                       + 5 * cp.abs(edge_DB) + 2 * cp.abs(edge_BC) + 7 * cp.abs(edge_BE))

prob = cp.Problem(maximize, constraints)

prob.solve()

print("The optimal value is", prob.value)
print("The value of edge_AD is", edge_AD.value)
print("The value of edge_AB is", edge_AB.value)
print("The value of edge_AC is", edge_AC.value)
print("The value of edge_DB is", edge_DB.value)
print("The value of edge_BC is", edge_BC.value)
print("The value of edge_BE is", edge_BE.value)
print("The value of edge_CE is", edge_CE.value)


edge_AD = cp.Variable(1, )
edge_AB = cp.Variable(1, )
edge_AC = cp.Variable(1, )
edge_DB = cp.Variable(1, )
edge_BC = cp.Variable(1, )
edge_BE = cp.Variable(1, )
edge_CE = cp.Variable(1, )

constraints = [edge_AD + edge_AB + edge_AC == -2,
               edge_DB - edge_AB == 7,
               - edge_DB - edge_AB + edge_BC == -2,
               -edge_AC - edge_BC + edge_CE == 3,
               -edge_BE - edge_CE == -6]

maximize = cp.Minimize(3 * cp.abs(edge_AD) + 6 * cp.abs(edge_AB) + 4 * cp.abs(edge_AC)
                       + 5 * cp.abs(edge_DB) + 2 * cp.abs(edge_BC) + 7 * cp.abs(edge_BE))

prob = cp.Problem(maximize, constraints)

prob.solve()

print("The optimal value is", prob.value)
print("The value of edge_AD is", edge_AD.value)
print("The value of edge_AB is", edge_AB.value)
print("The value of edge_AC is", edge_AC.value)
print("The value of edge_DB is", edge_DB.value)
print("The value of edge_BC is", edge_BC.value)
print("The value of edge_BE is", edge_BE.value)
print("The value of edge_CE is", edge_CE.value)
