import numpy as np
import random
from goza import Chart, Scatter, Bar, ECDF


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


def test_bar_figsize():

    x = ["A", "B", "C", "D"]
    y = [5, 4, 3, 2]

    bar = Bar(x, y, title="Bar Example")

    assert bar.figsize == (10, 8)


def test_ecdf():

    x = np.random.normal(size=1000)

    ecdf = ECDF(x)

    assert round(ecdf.y.mean(), 1) == 0.5
