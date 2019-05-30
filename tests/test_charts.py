import random
from goza import Chart, Scatter


def test_chart_spine():

    chart = Chart()

    assert chart.ax.spines["top"].get_visible()
    assert chart.ax.spines["right"].get_visible()


def test_chart_labels():

    chart = Chart("Test")

    assert chart.title == "Test"
    assert chart.xlabel == "X-Axis"


def test_scatter_data():

    x = random.sample(range(1, 100), 50)
    y = random.sample(range(1, 100), 50)

    scatter = Scatter(x, y, title="Scatter Example")

    assert len(scatter.x) == len(scatter.y)
