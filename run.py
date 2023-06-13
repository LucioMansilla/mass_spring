from euler_mass_spring import EulerMassSpring
from mass_spring_system import MassSpringSystem
import matplotlib.pyplot as plt
from parser import parser_arguments
from plotter import Plotter


if __name__ == '__main__':

    # Obtener los argumentos de la línea de comandos
    args = parser_arguments()

    #Crear el sistema de masa y resorte
    mass_spring_system = MassSpringSystem(mass=args.mass, spring_resistance=args.spring_resistance, friction=args.friction, force=args.force)

    # Crear el solver Euler para el sistema de masa y resorte
    e = EulerMassSpring(x0=args.x0, v0=args.v0, dt=args.dt, mass_spring_model=mass_spring_system)

    # Resolver el sistema
    x, v, t = e.solve(iterations=args.sim_time)

    # Graficar los resultados
    plotter = Plotter(x, v, t)
    plotter.plot()



