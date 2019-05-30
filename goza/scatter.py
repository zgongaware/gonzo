from goza import Chart


class Scatter(Chart):
    """

    """
    def __init__(self, x, y, title=None, xlabel=None, ylabel=None, figsize=None):

        self.x = x
        self.y = y

        # Initiate chart
        Chart.__init__(self, title, xlabel, ylabel, figsize)

        # Plot scatter plot
        self.plot_scatter()

        # Show
        self.show()

    def plot_scatter(self, color="black", size=2):

        self.ax.scatter(self.x, self.y, color=color, s=size)
