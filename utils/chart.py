from typing import Union, Callable, List, TypeVar, Dict, Iterable

from utils import underscore as _
import matplotlib.pyplot as plt

T = TypeVar('T')
K = TypeVar('K')

Optional = Union[T, None]
Number = Union[int, float]
ValueSelector = Callable[[T], Number]
ColorSelector = Callable[[T], str]
KeySelector = Callable[[T], K]


class Chart:
    def __init__(
            self,
            title: str = '',
            x_label: str = 'x',
            y_label: str = 'y',
            height: int = 1080,
            width: int = 1920
    ):
        fig, ax = plt.subplots(figsize=(width / 100.0, height / 100.0))
        self.fig = fig
        self.ax = ax
        if title != '':
            self.ax.set_title(title)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.grid(which='major')

    def line(
            self,
            x: List[Number],
            y: List[Number],
            label: str = '',
            color: str = '#1f77b4',
            style: str = '-'
    ):
        self.ax.plot(
            x,
            y,
            label=label,
            color=color,
            linestyle=style
        )

        if label != '':
            self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        return self

    def scatter(
            self,
            x: List[Number],
            y: List[Number],
            size: Optional[List[Number]] = None,
            color: Optional[Union[List[str], str]] = None,
            label: str = '',
            marker: str = 'x',
            alpha: float = 1.0
    ):
        if color is None:
            color = _.map(x, lambda _x: '#1f77b4')
        elif type(color) is str:
            color = _.map(x, lambda _x: color)
        if size is None:
            self.ax.scatter(
                x,
                y,
                color=color,
                marker=marker,
                alpha=alpha,
                label=label
            )
        else:
            self.ax.scatter(
                x,
                y,
                s=size,
                color=color,
                marker=marker,
                alpha=alpha,
                label=label
            )

        if label != '':
            self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        return self

    def line_data(
            self,
            data: List[T],
            x: ValueSelector[T],
            y: ValueSelector[T],
            color: str = '#1f77b4',
            style: str = '-'
    ):
        xAxis = []
        values = []
        for element in data:
            xAxis.append(x(element))
            values.append(y(element))
        self.ax.plot(
            xAxis,
            values,
            color=color,
            linestyle=style
        )
        return self

    def scatter_data(
            self,
            data: Iterable[T],
            x: ValueSelector[T],
            y: ValueSelector[T],
            size: Optional[ValueSelector[T]] = None,
            color: ColorSelector[T] = lambda _it: '#1f77b4',
            label: str = '',
            marker: str = 'x',
            alpha: float = 1.0
    ):
        _x = []
        _y = []
        _c = []
        _z = None if size is None else _.map(data, size)
        for element in data:
            _x.append(x(element))
            _y.append(y(element))
            _c.append(color(element))
        return self.scatter(
            _x,
            _y,
            size=_z,
            color=_c,
            label=label,
            marker=marker,
            alpha=alpha
        )

    def bar_data(
            self,
            data: List[T],
            x: KeySelector[T, K],
            y: ValueSelector[T]
    ):
        xAxis = []
        values = []
        for element in data:
            xAxis.append(x(element))
            values.append(y(element))
        self.ax.bar(
            xAxis,
            values
        )
        return self

    def bar_dict(
            self,
            dict: Dict[T, Number]
    ):
        xAxis = []
        values = []
        for x, element in dict.items():
            xAxis.append(x)
            values.append(element)
        self.ax.bar(
            xAxis,
            values
        )
        return self

    def show(self) -> None:
        self.fig.show()

    def save(self, filename: str) -> None:
        self.fig.savefig(filename)
