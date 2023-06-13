# Description: Parser de argumentos para la simulación de 
import argparse 

def parser_arguments():
    parser = argparse.ArgumentParser(description='Simulation Mass-Spring')
    parser.add_argument('mass', metavar='mass', help='Mass of the system', type=float)
    parser.add_argument('spring_resistance', help='Spring resistance', type=float)
    parser.add_argument('friction', help='Friction', type=float)
    parser.add_argument('force', help='Force', type=float)
    parser.add_argument('-dt', '--delta_time', help='Delta time', type=float, default=0.001)
    parser.add_argument('-t', '--sim_time', help='SimTime', type=float, default=10)
    parser.add_argument('-x', '--position_initial', help='Position initial', type=float, default=0)
    parser.add_argument('-v', '--velocity_initial', help='Velocity initial', type=float, default=0)
    return parser.parse_args()


