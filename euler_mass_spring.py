class EulerMassSpring:
    def __init__(self, x0, v0, dt, mass_spring_model):
        self.x = [x0]
        self.v = [v0]
        self.t = [0.0]
        self.dt = dt
        self.model = mass_spring_model
        self.oscillations = 0
        self.previous_v_sign = self.sign(v0)

    def sign(self, num):
        return 1 if num >= 0 else -1

    def step(self):
        self.x.append(self.x[-1] + self.dt * self.model.derivate_of_x(self.v))
        new_v = self.v[-1] + self.dt * self.model.derivate_of_v(self.v,self.x)
        self.v.append(new_v)
        self.t.append(self.t[-1] + self.dt)

        current_v_sign = self.sign(new_v)
        if current_v_sign != self.previous_v_sign:
            self.oscillations += 1
        self.previous_v_sign = current_v_sign

    def solve(self, iterations):
        while self.t[-1] < iterations:
            self.step()
        return self.x, self.v, self.t, self.oscillations





   


