class MassSpringSystem:
    """
    Modelo de un sistema masa-resorte.

    Args:
        mass (float): Masa del objeto.
        spring_resistance (float): Constante de resistencia del resorte.
        friction (float): Coeficiente de fricción.
        force (float): Fuerza aplicada.
    """

    def __init__(self, mass:float, spring_resistance:float, friction:float, force:float):
        self.mass = mass
        self.spring_resistance = spring_resistance
        self.friction = friction
        self.force = force

    def derivate_of_v(self, v:list[float], x:list[float]) -> float:
        """
        Calcula la derivada de la velocidad en función de la posición.

        Args:
            v (list): Lista de velocidades en diferentes instantes de tiempo.
            x (list): Lista de posiciones en diferentes instantes de tiempo.

        Returns:
            float: Derivada de la velocidad.
        """
        return (-self.spring_resistance / self.mass) * x[-1] - (self.friction/self.mass)* v[-1] + self.force/self.mass

    def derivate_of_x(self, v:list[float]) -> float: 
        """
        Calcula la derivada de la posición en función de la velocidad.

        Args:
            v (list): Lista de velocidades en diferentes instantes de tiempo.

        Returns:
            float: Derivada de la posición (velocidad).
        """
        return v[-1]