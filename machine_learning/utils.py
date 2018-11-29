import random
from typing import List, TypeVar, Callable, Tuple

T = TypeVar('T')
K = TypeVar('K')
KeySelector = Callable[[T], K]

def train_and_test(
        data: List[T],
        by=KeySelector[T, K],
        train_size: float = .8,
        shuffle: bool = True
) -> Tuple[List[T], List[T]]:
    group_by_key = _.group_by(data, by)
    train_set = []
    test_set = []
    for key, list in group_by_key.items():
        if shuffle:
            random.shuffle(list)
        cut_index = int(train_size * len(list))
        train_set += list[0:cut_index]
        test_set += list[cut_index:len(list)]
    return train_set, test_set