class MassSpringSystem:
    """
    Model of a mass-spring system.

    Args:
        mass (float): Mass of the object.
        spring_resistance (float): Spring resistance constant.
        friction (float): Friction coefficient.
        force (float): Applied force.
    """

    def __init__(
        self, mass: float, spring_resistance: float, friction: float, force: float
    ):
        self.mass = mass
        self.spring_resistance = spring_resistance
        self.friction = friction
        self.force = force


    def __str__(self):
        """
        Returns a string representation of the model.
        """
        return f"mass={self.mass}, spring resistance={self.spring_resistance}, friction={self.friction}, force={self.force}"

    def derivate_of_v(self, v: list[float], x: list[float]) -> float:
        """
        Calculates the derivative of velocity with respect to position.

        Args:
            v (list): List of velocities at different time instants.
            x (list): List of positions at different time instants.

        Returns:
            float: Derivative of velocity.
        """
        return (
            (-self.spring_resistance / self.mass) * x[-1]
            - (self.friction / self.mass) * v[-1]
            + self.force / self.mass
        )

    def derivate_of_x(self, v: list[float]) -> float:
        """
        Calculates the derivative of position with respect to velocity.

        Args:
            v (list): List of velocities at different time instants.

        Returns:
            float: Derivative of position (velocity).
        """
        return v[-1]
