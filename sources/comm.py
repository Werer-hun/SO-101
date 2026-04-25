#asks for angels to rotate the joints 
class communication:
    @staticmethod
    def ask_for_angles(n_joints):
        angles = []
        for i in range(n_joints):
            angle = float(input("Enter angle for joint {}: ".format(i+1)))
            angles.append(angle)
        return angles

    @staticmethod
    def print_angles(angles):
       for i, angle in enumerate(angles):
            print("Joint {}: {} degrees".format(i+1, angle))