import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FuncAnimation

class Plotter:
    """
    Class for plotting the position and velocity of various models over time.

    Args:
        data (dict): A dictionary where keys are model names and values are the corresponding data. 
    """
    def __init__(self, data):
        self.data = data

    def plot(self):
        """
        Plots position and velocity as a function of time for each model.
        """
        fig, axs = plt.subplots(2)
        
        for model, model_data in self.data.items():
            x, v, t = model_data

            label = str(model)

            # Plot of position as a function of time
            axs[0].plot(t, x, label=label)
            
            # Plot of velocity as a function of time
            axs[1].plot(t, v, label=label)

        axs[0].set_title('Position as a Function of Time')
        axs[0].set(xlabel='Time', ylabel='Position')
        axs[0].legend()

        axs[1].set_title('Velocity as a Function of Time')
        axs[1].set(xlabel='Time', ylabel='Velocity')
        axs[1].legend()

        plt.tight_layout()
        plt.show()


class AnimationPlotter:
    """
    Class for creating an animated plot of the position and velocity of various models over time.

    Args:
        euler_mass_spring_models (list): A list of EulerMassSpring model instances to be animated.
    """
    def __init__(self, euler_mass_spring_models):
        self.models = euler_mass_spring_models
        self.t = np.linspace(0, 50, 100)  # Define the time range and resolution

    def animate(self, i):
        """
        Function to animate the position and velocity plots.

        Args:
            i (int): Current frame number.

        Returns:
            Updated plot lines.
        """
        artists = []
        for line, model in zip(self.lines, self.models):
            x, v, t, oscillations = model.solve(iterations=self.t[i])  # Use t[i] instead of i*10
            line[0].set_data(t, x)  # Update the position plot
            line[1].set_data(t, v)  # Update the velocity plot
            line[0].axes.set_xlim(t[0], t[-1])  # Update the x-axis limits for the position plot
            line[1].axes.set_xlim(t[0], t[-1])  # Update the x-axis limits for the velocity plot
            line[0].axes.set_ylim(-0.1, 3.7)  # Set y-axis limits for the position plot
            line[1].axes.set_ylim(-0.30, 1.6)  # Set y-axis limits for the velocity plot
            artists.extend(line)
        return artists

    def plot(self):
        """
        Sets up the position and velocity plots and initiates the animation.
        """
        fig, axs = plt.subplots(2)

        self.lines = []
        for model in self.models:
            # Create a line for each model in both the position and velocity plots
            line1, = axs[0].plot([], [], label=f'm={model.model.force}')
            line2, = axs[1].plot([], [], label=f'm={model.model.force}')
            self.lines.append((line1, line2))

        axs[0].set_title('Position as a Function of Time')
        axs[0].set(xlabel='Time', ylabel='Position')
        axs[0].legend()

        axs[1].set_title('Velocity as a Function of Time')
        axs[1].set(xlabel='Time', ylabel='Velocity')
        axs[1].legend()

        # Set up the animation
        ani = MyFuncAnimation(fig, self.animate, frames=len(self.t), interval=20, blit=True)  # Use len(t) frames
        ani.save("animation.mp4", writer='ffmpeg')
        plt.subplots_adjust(hspace = 2)
        plt.tight_layout()
        plt.show()


class MyFuncAnimation(FuncAnimation):
    def _stop(self, *args):
        """
        Overridden function from FuncAnimation class to stop the animation.
        """
        self.event_source.remove_callback(self._step)
        self.event_source = None

