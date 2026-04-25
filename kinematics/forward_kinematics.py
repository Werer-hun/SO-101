import numpy as np
from utils.quaternions import Quat_operations
from sources.comm import communication

class FK:
    def __init__(self):
        # Most már elmentjük, melyik csukló melyik tengely körül forog
        # 'z' = függőleges forgás, 'y' = hajlítás
        self.joint_config = [
            {'offset': [0, 0, 0.04115], 'axis': 'z'}, # torso
            {'offset': [0, 0, 0],       'axis': 'z'}, # shoulder_pan
            {'offset': [0, 0.012, 0.05],'axis': 'y'}, # shoulder_lift (HAJLIK!)
            {'offset': [0.0001, 0, 0.1],'axis': 'y'}, # elbow_flex (HAJLIK!)
            {'offset': [0, 0, 0.1],     'axis': 'y'}, # wrist_flex
            {'offset': [0, 0, 0.065],    'axis': 'z'} # wrist_roll
        ]
        
        self.angles = communication.ask_for_angles(len(self.joint_config))
        
    @staticmethod
    def calc_all_quat(angles, joint_config):
        quats = []
        for i, joint in enumerate(joint_config):
            if joint['axis'] == 'z':
                q = Quat_operations.axis_angle_to_quat([0, 0, 1], angles[i])
            elif joint['axis'] == 'y':
                q = Quat_operations.axis_angle_to_quat([0, 1, 0], angles[i])
            elif joint['axis'] == 'x':
                q = Quat_operations.axis_angle_to_quat([1, 0, 0], angles[i])
            quats.append(q)
        return quats
    
    @staticmethod
    def get_transformations(quats, joint_config):
        transformations = []
        for i, joint in enumerate(joint_config):
            R = Quat_operations.qaut_to_rot_matrix(quats[i])
            T = np.eye(4)
            T[:3, :3] = R
            T[:3, 3] = joint['offset']
            transformations.append(T)
        return transformations
    @staticmethod
    def end_effector_pose(transformations):
        T_total = np.eye(4)
        for T in transformations:
            T_total = T_total @ T
        return T_total