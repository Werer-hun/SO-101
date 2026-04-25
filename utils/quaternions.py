import numpy as np
class Quat_operations:
    @staticmethod
    def axis_angle_to_quat(axis, angle_deg):
        #Egy tengely és szög -> [w, x, y, z] kvaternió
        angle_rad = np.radians(angle_deg)
        axis = np.array(axis) / np.linalg.norm(axis)
        s = np.sin(angle_rad / 2)
        return np.array([np.cos(angle_rad / 2), axis[0]*s, axis[1]*s, axis[2]*s])

    @staticmethod
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

    @staticmethod
    def qaut_rot_matrix(q):
        #Kvaternió -> 3x3 forgatási mátrix
        w, x, y, z = q
        return np.array([
            [w**2 + x**2 - y**2 - z**2, 2*(x*y - w*z), 2*(x*z + w*y)],
            [2*(x*y + w*z), w**2 - x**2 + y**2 - z**2, 2*(y*z - w*x)],
            [2*(x*z - w*y), 2*(y*z + w*x), w**2 - x**2 - y**2 + z**2]
        ])
    @staticmethod
    def rot_matrix_to_euler(R):
        #3x3 forgatási mátrix -> Euler szögek (roll, pitch, yaw)
        sy = np.sqrt(R[0,0]**2 + R[1,0]**2)
        singular = sy < 1e-6
        if not singular:
            roll = np.arctan2(R[2,1], R[2,2])
            pitch = np.arctan2(-R[2,0], sy)
            yaw = np.arctan2(R[1,0], R[0,0])
        else:
            roll = np.arctan2(-R[1,2], R[1,1])
            pitch = np.arctan2(-R[2,0], sy)
            yaw = 0
        return np.degrees([roll, pitch, yaw])