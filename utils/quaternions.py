import numpy as np

def axis_angle_to_quat(axis, angle_deg):
    #Egy tengely és szög -> [w, x, y, z] kvaternió
    angle_rad = np.radians(angle_deg)
    axis = np.array(axis) / np.linalg.norm(axis)
    s = np.sin(angle_rad / 2)
    return np.array([np.cos(angle_rad / 2), axis[0]*s, axis[1]*s, axis[2]*s])

def quat_multiply(q1, q2):
    #Két kvaternió [w, x, y, z] összeszorzása mátrixok nélkül
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])


def qaut_rot_matrix(q):
    #Kvaternió -> 3x3 forgatási mátrix
    w, x, y, z = q
    return np.array([
        [w**2 + x**2 - y**2 - z**2, 2*(x*y - w*z), 2*(x*z + w*y)],
        [2*(x*y + w*z), w**2 - x**2 + y**2 - z**2, 2*(y*z - w*x)],
        [2*(x*z - w*y), 2*(y*z + w*x), w**2 - x**2 - y**2 + z**2]
    ])