#asks for angels to rotate the joints 
def ask_for_angles(n_joints):
    angles = []
    for i in range(n_joints):
        angle = float(input("Enter angle for joint {}: ".format(i+1)))
        angles.append(angle)
    return angles