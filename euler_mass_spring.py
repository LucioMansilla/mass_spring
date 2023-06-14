from mass_spring_system import MassSpringSystem
class EulerMassSpring:
    """
    Clase que implementa el método de Euler para resolver el sistema masa-resorte.

    Args:
        x0 (float): Posición inicial.
        v0 (float): Velocidad inicial.
        dt (float): Paso de tiempo de la simulación.
        mass_spring_model (MassSpringSystem): Modelo de sistema masa-resorte.
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
        Calcula el signo de un número dado.

        Args:
            num (float): Número a evaluar.

        Returns:
            int: 1 si el número es positivo, -1 en caso contrario.
        """
        return 1 if num >= 0 else -1

    def step(self):
        """
        Realiza un paso en la simulación del sistema masa-resorte.
        Actualiza la posición, velocidad y tiempo en cada paso.
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
        Resuelve el sistema masa-resorte hasta un tiempo dado.

        Args:
            iterations (int): Tiempo hasta el cual se resuelve el sistema.

        Returns:
            tuple: Lista de posiciones, velocidades, tiempos y cantidad de oscilaciones.
        """
        while self.t[-1] < iterations:
            self.step()
        return self.x, self.v, self.t, self.oscillations





   


