import numpy as np
import pyswarms as ps
from math import cos, sin, radians


def delta(target, current):
    x = (target[0] - current[0])**2
    y = (target[1] - current[1])**2
    z = (target[2] - current[2])**2
    dist = np.sqrt(x + y + z)
    return dist

def fwkinematics(param):
    l1 = 80
    l2 = 80
    l3 = 80
    l4 = 80
    rx = l2 * cos(radians(param[1])) + l3 * cos(radians(param[2])) + l4 * cos(radians(param[3]))
    y = l1 + l2 * sin(radians(param[1])) + l3 * sin(radians(param[2])) + l4 * sin(radians(param[3]))
    z = rx * cos(radians(param[0]))
    x = rx * sin(radians(param[0]))
    return np.array([x,y,z])

def opt_func(X):
    n_particles = X.shape[0]  # number of particles
    target = np.array([-2,2,3])
    dist = [delta(fwkinematics(X[i]), target) for i in range(n_particles)]
    return np.array(dist)


target = [2, 4, 6]

swarm_size = 20
dim = 4        # Dimension of X
epsilon = 1.0
options = {'c1': 1.5, 'c2':1.5, 'w':0.5}

constraints = (np.array([-60, -60, -60, -60]),
               np.array([60, 60, 60, 60]))

d1 = d2 = d3 = d4 = 80


# Call an instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=swarm_size,
                                    dimensions=dim,
                                    options=options,
                                    bounds=constraints)

# Perform optimization
cost, joint_vars = optimizer.optimize(opt_func, iters=100)

print(fwkinematics(joint_vars))
