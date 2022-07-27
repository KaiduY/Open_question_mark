import ikpy.chain
import numpy as np
import ikpy.utils.plot as plot_utils
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink, DHLink

robotarm = Chain(name='robotarm', links=[
    OriginLink(),
    DHLink(
        name='base',
        bounds=(-np.pi/3, np.pi/3),
        d=80,
        a=90,
    ),
    DHLink(
        name='base',
        bounds=(-np.pi/3, np.pi/3),
        d=80,
        a=0,
    ),
    DHLink(
        name='base',
        bounds=(-np.pi/3, np.pi/3),
        d=80,
        a=0,
    ),
    DHLink(
        name='base',
        bounds=(-np.pi/3, np.pi/3),
        d=80,
        a=0,
    )
])

target_position = [ 0.1, -0.2, 0.1]
print("The angles of each joints are : ", robotarm.inverse_kinematics(target_position))