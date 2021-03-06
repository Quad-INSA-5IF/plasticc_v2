from typing import Callable, TypeVar, List, Tuple, Generic

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
K = TypeVar('K')

KeySelector = Callable[[T], K]
Transform = Callable[[T], U]

class Feature(Generic[T]):
    def __init__(self, description: str, accept: Callable[[T], bool]):
        self.description = description
        self.accept = accept

    def split(self, data: List[T]) -> Tuple[List[T], List[T]]:
        belongs = []
        not_belongs = []
        for element in data:
            if self.accept(element):
                belongs.append(element)
            else:
                not_belongs.append(element)
        return belongs, not_belongs

    def __and__(self, other):
        assert type(other) is Feature[T]
        description = self.description + " and " + other.description
        return Feature(description, lambda x: self.accept(x) and other.accept(x))

    def __repr__(self):
        return f'(is {self.description} ?)'


class Property(Generic[T, U]):
    def __init__(self, name: str, selector: Callable[[T], U]):
        self.name = name
        self.of = selector

    def memoize(self):
        cache = {}

        def get(element: T) -> U:
            if element not in cache:
                cache[element] = self.of(element)
            return cache[element]

        return Property(name='[mem]' + self.name, selector=get)

    def __lt__(self, value: U) -> Feature:
        return Feature(
            description=f'{self.name} < {value}',
            accept=lambda x: self.of(x) < value
        )

    def __gt__(self, value: U) -> Feature:
        return Feature(
            description=f'{self.name} > {value}',
            accept=lambda x: self.of(x) > value
        )

    def __le__(self, value: U) -> Feature:
        return Feature(
            description=f'{self.name} <= {value}',
            accept=lambda x: self.of(x) <= value
        )

    def __ge__(self, value: U) -> Feature:
        return Feature(
            description=f'{self.name} >= {value}',
            accept=lambda x: self.of(x) >= value
        )

    def __eq__(self, value: U) -> Feature:
        return Feature(
            description=f'{self.name} == {value}',
            accept=lambda x: self.of(x) == value
        )

    def __ne__(self, value: U) -> Feature:
        return Feature(
            description=f'{self.name} != {value}',
            accept=lambda x: self.of(x) != value
        )

    def __add__(self, value):
        return Property(
            name=f'{self.name} + {value}',
            selector=lambda x: self.of(x) + value
        )

    def __sub__(self, value):
        return Property(
            name=f'{self.name} - {value}',
            selector=lambda x: self.of(x) - value
        )