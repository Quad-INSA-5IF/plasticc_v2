import random
from typing import List, Dict, TypeVar, Callable, Union, Any, Iterable, Tuple

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')
U = TypeVar('U')

Predicate = Callable[[T], bool]
Consumer = Callable[[T], None]
Transform = Callable[[T], U]
KeySelector = Callable[[T], K]
Option = Union[T, None]


def identity(it: Any) -> Any:
    return it


def each(iter: Iterable[T], func: Consumer[T]) -> None:
    for data in iter:
        func(data)


def map(iter: Iterable[T], transform: Transform[T, U]) -> List[U]:
    result = []
    for data in iter:
        result.append(transform(data))
    return result


def find(list: List[T], predicate: Predicate[T]) -> Union[U, None]:
    for data in list:
        if predicate(data):
            return data
    return None


def filter(iter: Iterable[T], predicate: Predicate[T]) -> List[T]:
    result = []
    for data in iter:
        if predicate(data):
            result.append(data)
    return result


def reject(iter: Iterable[T], predicate: Predicate[T]) -> List[T]:
    result = []
    for data in iter:
        if not predicate(data):
            result.append(data)
    return result


def max_by(iter: Iterable[T], by: KeySelector[T, K]) -> Union[T, None]:
    max_key = None
    max_data = None
    for data in iter:
        key = by(data)
        if max_key is None or key > max_key:
            max_key = key
            max_data = data
    return max_data


def min_by(iter: List[T], by: KeySelector[T, K]) -> Union[T, None]:
    min_key = None
    min_data = None
    for data in iter:
        key = by(data)
        if min_key is None or key < min_key:
            min_key = key
            min_data = data
    return min_data


def min_float(iter: Iterable[float]) -> Union[float, None]:
    min = None
    for x in iter:
        if min is None or x < min:
            min = x
    return min


def all(iter: Iterable[T], predicate: Predicate[T]) -> bool:
    for data in iter:
        if not predicate(data):
            return False
    return True


def any(iter: Iterable[T], predicate: Predicate[T]) -> bool:
    for data in iter:
        if predicate(data):
            return True
    return False


def sort(iter: Iterable[T]) -> List[T]:
    return sorted(iter)


def sort_by(iter: Iterable[T], by: KeySelector[T, K]) -> List[T]:
    return sorted(iter, key=by)


def group_by(iter: Iterable[T], by: KeySelector[T, K]) -> Dict[K, List[T]]:
    result = {}
    for data in iter:
        key = by(data)
        list_for_key = result[key] if key in result else []
        list_for_key.append(data)
        result[key] = list_for_key
    return result


def distinct(iter: Iterable[T]) -> List[T]:
    result = []
    for data in iter:
        if data not in result:
            result.append(data)
    return result


def distinct_by(iter: Iterable[T], by: KeySelector[T, K]) -> List[T]:
    keys = []
    result = []
    for data in iter:
        key = by(data)
        if key not in keys:
            keys.append(key)
            result.append(data)
    return result


def flatten(iter: Iterable[Iterable[T]]) -> List[T]:
    result = []
    for sublist in iter:
        result += sublist
    return result


def index_by(iter: Iterable[T], by: KeySelector[T, K]) -> Dict[K, T]:
    result = {}
    for data in iter:
        result[by(data)] = data
    return result


def count(iter: Iterable[T], predicate: Predicate[T]) -> int:
    c = 0
    for data in iter:
        if predicate(data):
            c += 1
    return c


def count_by(iter: Iterable[T], by: KeySelector[T, K] = identity) -> Dict[K, int]:
    result = {}
    for data in iter:
        key = by(data)
        count_for_key = result[key] if key in result else 0
        count_for_key += 1
        result[key] = count_for_key
    return result


def partition_by(
        iter: Iterable[T],
        predicate: Predicate[T]
) -> Tuple[List[T], List[T]]:
    trues = []
    falsies = []
    for data in iter:
        if predicate(data):
            trues.append(data)
        else:
            falsies.append(data)
    return trues, falsies


def percentile_by(
        iter: Iterable[T],
        percentile: float,
        by: KeySelector[T, K],
        is_sorted: bool = False
) -> Union[T, None]:
    if len(iter) == 0:
        return None
    else:
        sorted_list = sort_by(iter, by=by) if not is_sorted else iter
        return sorted_list[int(percentile * len(iter) / 100)]


def take(iter: Iterable[T], n: int) -> List[T]:
    result = []
    for data in iter:
        if len(result) == n:
            break
        else:
            result.append(data)
    return result

def train_and_test(
        iter: Iterable[T],
        by: KeySelector[T, K],
        shuffle: bool = True,
        train: float = 0.8
) -> Tuple[List[T], List[T]]:
    train_set = []
    test_set = []
    for _id, objects in group_by(iter, by).items():
        if shuffle:
            random.shuffle(objects)
        n = int(train * len(objects))
        train_set += objects[0:n]
        test_set += objects[n:len(objects)]

    random.shuffle(train_set)
    random.shuffle(test_set)
    return train_set, test_set


def sum_double_by(
        iter: Iterable[T],
        by: KeySelector[T, float]
) -> float:
    sum = 0.0
    count = 0
    for data in iter:
        sum += by(data)
        count += 1
    return sum / float(count)


def max(iter: Iterable[T]) -> Option[T]:
    best = None
    for data in iter:
        if best is None or data > best:
            best = data
    return best