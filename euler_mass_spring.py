from mass_spring_system import MassSpringSystem
class EulerMassSpring:
    """
    Class that implements the Euler method for solving the mass-spring system.

    Args:
        x0 (float): Initial position.
        v0 (float): Initial velocity.
        dt (float): Time step of the simulation.
        mass_spring_model (MassSpringSystem): Mass-spring system model.
    """

    def __init__(self, x0:float, v0:float, dt:float, mass_spring_model:MassSpringSystem):
        self.x = [x0]
        self.v = [v0]
        self.t = [0.0]
        self.dt = dt
        self.model = mass_spring_model
        self.oscillations = 0
        self.previous_v_sign = self.sign(v0)

    def sign(self, num:float) -> int:
        """
        Calculates the sign of a given number.

        Args:
            num (float): Number to evaluate.

        Returns:
            int: 1 if the number is positive, -1 otherwise.

        """
        return 1 if num >= 0 else -1

    def step(self):
        """
        Perform a step in the mass-spring system simulation.
        Update the position, velocity, and time at each step.
        """
        self.x.append(self.x[-1] + self.dt * self.model.derivate_of_x(self.v))
        new_v = self.v[-1] + self.dt * self.model.derivate_of_v(self.v,self.x)
        self.v.append(new_v)
        self.t.append(self.t[-1] + self.dt)

        current_v_sign = self.sign(new_v)
        if current_v_sign != self.previous_v_sign:
            self.oscillations += 1
        self.previous_v_sign = current_v_sign

    def solve(self, iterations:int):
        """
        Solves the mass-spring system up to a given time.

        Args:
            iterations (int): Time until which the system is solved.

        Returns:
            tuple: List of positions, velocities, times, and number of oscillations.
        """
        while self.t[-1] < iterations:
            self.step()
        return self.x, self.v, self.t, self.oscillations





   


