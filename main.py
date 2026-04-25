import numpy as np
from utils.quaternions import Quat_operations
from sources.comm import communication
from kinematics.forward_kinematics import FK

robot=joint_config = [
            {'offset': [0, 0, 0.04115], 'axis': 'z'}, # torso
            {'offset': [0, 0, 0],       'axis': 'z'}, # shoulder_pan
            {'offset': [0, 0.012, 0.05],'axis': 'y'}, # shoulder_lift (HAJLIK!)
            {'offset': [0.0001, 0, 0.1],'axis': 'y'}, # elbow_flex (HAJLIK!)
            {'offset': [0, 0, 0.1],     'axis': 'y'}, # wrist_flex
            {'offset': [0, 0, 0.065],    'axis': 'z'} # wrist_roll
        ]
angles = communication.ask_for_angles(len(robot))
quats = FK.calc_all_quat(angles, robot)

transformations = FK.get_transformations(quats, robot)

T_total = FK.end_effector_pose(transformations)


orientation = Quat_operations.rot_matrix_to_euler(T_total[:3, :3])
position = T_total[:3, 3]
print("End Effector Position: ", position)
print("End Effector Orientation (roll, pitch, yaw): ", orientation)