import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, euler_mass_spring_models):
        self.models = euler_mass_spring_models

    def plot(self):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        fig, axs = plt.subplots(2)

        for model in self.models:
            x, v, t, oscillations = model.solve(iterations=100)

            # Gráfico de la posición en función del tiempo
            axs[0].plot(t, x, label=f'm={model.model.mass}')
            
            # Gráfico de la velocidad en función del tiempo
            axs[1].plot(t, v, label=f'm={model.model.mass}')
            
            # Mostrar el número de oscilaciones
            print(f'Para m={model.model.mass} se realizaron {oscillations} oscilaciones')

        axs[0].set_title('Posición en función del tiempo')
        axs[0].set(xlabel='Tiempo', ylabel='Posición')
        axs[0].legend()

        axs[1].set_title('Velocidad en función del tiempo')
        axs[1].set(xlabel='Tiempo', ylabel='Velocidad')
        axs[1].legend()

        plt.tight_layout()
        plt.show()