class MassSpringSystem:
    def __init__(self, mass, spring_resistance, friction, force):
        self.mass = mass
        self.spring_resistance = spring_resistance
        self.friction = friction
        self.force = force

    def derivate_of_v(self,v,x):
        return (-self.spring_resistance / self.mass) * x[-1] - (self.friction/self.mass)* v[-1] + self.force/self.mass

    def derivate_of_x(self,v): 
        return v[-1]