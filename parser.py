import argparse 

def parser_arguments() -> argparse:
    """
    Creates and returns an object that contains the arguments passed through the command line.

    Returns:
        (argparse): Object that contains the arguments for simulating the mass-spring system.
    """
    parser = argparse.ArgumentParser(description='Simulation Mass-Spring')
    parser.add_argument('-mass', type=float, help='Mass')
    parser.add_argument('-spring_resistance', type=float, help='Spring resistance')
    parser.add_argument('-friction', type=float, help='Friction')
    parser.add_argument('-force', type=float, help='Force')
    parser.add_argument('-dt', type=float, help='Delta time', default=0.001)
    parser.add_argument('-t', type=float, help='Time', default=100, dest="sim_time")
    parser.add_argument('-x', type=float, help='Position initial', default=0)
    parser.add_argument('-v', type=float, help='Velocity initial', default=0)
    return parser.parse_args()


