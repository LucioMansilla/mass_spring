from euler_mass_spring import EulerMassSpring
from mass_spring_system import MassSpringSystem
from parser import parser_arguments
from plotter import Plotter
from prettytable import PrettyTable


def report(models_data):
    """
    Generate a report table from the data of multiple models.
    """
    table = PrettyTable()

    table.field_names = [
        "Model",
        "Oscillations",
        "Max Velocity",
        "Max Position",
        "Min Velocity",
        "Min Position",
    ]

    for model, data in models_data.items():
        x, v, t, oscillations = data
        table.add_row([model, oscillations, max(v), max(x), min(v), min(x)])

    print(table)
  
if __name__ == "__main__":
    # Get the command line arguments
    args = parser_arguments()

    # Create the mass and spring system
    mass_spring_system = MassSpringSystem(
        mass=args.mass,
        spring_resistance=args.spring_resistance,
        friction=args.friction,
        force=args.force,
    )

    # Create the Euler solver for the mass and spring system
    e = EulerMassSpring(
        x0=args.x, v0=args.v, dt=args.dt, mass_spring_model=mass_spring_system
    )

    # Solve the system
    x, v, t, oscillations = e.solve(iterations=args.sim_time)

    # Prepare the data for the Plotter
    data = {e.model: (x, v, t)}

    # Plot the results
    plotter = Plotter(data)
    plotter.plot()

    # Generate the report
    data_report = {e.model: (x, v, t, oscillations)}
    report(data_report)
