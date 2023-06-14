from euler_mass_spring import EulerMassSpring
from mass_spring_system import MassSpringSystem
from plotter import Plotter, AnimationPlotter

def mass_experiments():
    # Crear los sistemas de masa y resorte
    mass_spring_system1 = MassSpringSystem(mass=1.0, spring_resistance=1.0, friction=1.0, force=1.0)
    mass_spring_system2 = MassSpringSystem(mass=4.0, spring_resistance=1.0, friction=1.0, force=1.0)

    # Crear los solvers Euler para los sistemas de masa y resorte
    e1 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system1)
    e2 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system2)

    # Crear el plotter y pasarle los modelos a graficar
    p = Plotter([e1, e2])
    p.plot()

def friction_experiments():

    mass_spring_system1 = MassSpringSystem(mass=1.0, spring_resistance=1.0, friction=1.0, force=1.0)
    mass_spring_system2 = MassSpringSystem(mass=1.0, spring_resistance=1.0, friction=0.0, force=1.0)

    e1 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system1)
    e2 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system2)

    #p = Plotter([e1, e2],100)
    #p.plot()

    p = AnimationPlotter([e1, e2])
    p.plot()    

def force_experiments():
    mass_spring_system1 = MassSpringSystem(mass=1.0, spring_resistance=1.0, friction=1.0, force=1.0)
    mass_spring_system2 = MassSpringSystem(mass=1.0, spring_resistance=1.0, friction=1.0, force=2.0)
    mass_spring_system3 = MassSpringSystem(mass=1.0, spring_resistance=1.0, friction=1.0, force=3.0)

    e1 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system1)
    e2 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system2)
    e3 = EulerMassSpring(x0=0, v0=0, dt=0.001, mass_spring_model=mass_spring_system3)

    p = AnimationPlotter([e1, e2, e3])
    p.plot()

if __name__ == '__main__':
    #mass_experiments()
    #friction_experiments()
    force_experiments()

