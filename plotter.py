import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FuncAnimation


class Plotter:
    def __init__(self, euler_mass_spring_models):
        self.models = euler_mass_spring_models

    def plot(self):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        fig, axs = plt.subplots(2)

        for model in self.models:
            x, v, t, oscillations = model.solve(iterations=50)

            # Plot of position as a function of time
            axs[0].plot(t, x, label=f'm={model.model.mass}')
            
            # Plot of velocity as a function of time
            axs[1].plot(t, v, label=f'm={model.model.mass}')
            
            # Display the number of oscillations
            print(f'For m={model.model.mass}, {oscillations} oscillations were performed')

        axs[0].set_title('Position as a Function of Time')
        axs[0].set(xlabel='Time', ylabel='Position')
        axs[0].legend()

        axs[1].set_title('Velocity as a Function of Time')
        axs[1].set(xlabel='Time', ylabel='Velocity')
        axs[1].legend()

        plt.tight_layout()
        plt.show()



class AnimationPlotter:
    def __init__(self, euler_mass_spring_models):
        self.models = euler_mass_spring_models
        self.t = np.linspace(0, 1000, 400)  # Define the time range and resolution

    def animate(self, i):
        artists = []
        for line, model in zip(self.lines, self.models):
            x, v, t, oscillations = model.solve(iterations=self.t[i])  # Use t[i] instead of i*10
            line[0].set_data(t, x)  # Update the position plot
            line[1].set_data(t, v)  # Update the velocity plot
            line[0].axes.set_xlim(t[0], t[-1])  # Update the x-axis limits for the position plot
            line[1].axes.set_xlim(t[0], t[-1])  # Update the x-axis limits for the velocity plot
            line[0].axes.set_ylim(-0.5, 2.3)  # Set y-axis limits for the position plot
            line[1].axes.set_ylim(-1.3, 1.3)  # Set y-axis limits for the velocity plot
            artists.extend(line)
        return artists



    def plot(self):
        fig, axs = plt.subplots(2)

        self.lines = []
        for model in self.models:
            # Create a line for each model in both the position and velocity plots
            line1, = axs[0].plot([], [], label=f'm={model.model.mass}')
            line2, = axs[1].plot([], [], label=f'm={model.model.mass}')
            self.lines.append((line1, line2))

        axs[0].set_title('Position as a Function of Time')
        axs[0].set(xlabel='Time', ylabel='Position')
        axs[0].legend()

        axs[1].set_title('Velocity as a Function of Time')
        axs[1].set(xlabel='Time', ylabel='Velocity')
        axs[1].legend()

        # Set up the animation
        ani = MyFuncAnimation(fig, self.animate, frames=len(self.t), interval=20, blit=True)  # Use len(t) frames
        ani.save("animation.mp4", writer='Pillow')
        plt.subplots_adjust(hspace = 2)
        plt.tight_layout()
        plt.show()


class MyFuncAnimation(FuncAnimation):
    def _stop(self, *args):
        self.event_source.remove_callback(self._step)
        self.event_source = None