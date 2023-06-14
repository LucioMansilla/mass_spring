from euler_mass_spring import EulerMassSpring
from mass_spring_system import MassSpringSystem
from plotter import Plotter, AnimationPlotter
from constants import *

def run_experiment(parameters, animation=False, iterations=DEFAULT_ITERATIONS):
    """
    Conducts an experiment on mass-spring systems with different parameters.
    Animates or plots the resulting systems' behaviors using the Euler's method solver.

    Args: parameters (list): A list of dictionaries containing the parameters for each system.
          animation (bool): If True, animates the systems' behaviors. Otherwise, plots the systems' behaviors.
          iterations (int): The number of iterations to run the simulation.
    """
    systems = [MassSpringSystem(**params) for params in parameters]
    solvers = [EulerMassSpring(x0=0, v0=0, dt=DEFAULT_STEP, mass_spring_model=system) for system in systems]

    if animation:
        p = AnimationPlotter(solvers)
        p.plot()
    else:
        data = {}
        for solver in solvers:
            x, v, t, oscillations = solver.solve(iterations)
            data.update({solver.model: (x, v, t)})

        plotter = Plotter(data)
        plotter.plot()


if __name__ == '__main__':

    # Experiment with different masses
    run_experiment(MASS_EXPERIMENT_PARAMS, animation=True)

    # Experiment with different friction coefficients
    run_experiment(FRICTION_EXPERIMENT_PARAMS)

    # Experiment with different external forces
    run_experiment(FORCE_EXPERIMENT_PARAMS)
