from typing import List, Callable, TypeVar, Union

T = TypeVar('T')


def read_csv(
        file_path: str,
        has_header: bool,
        transform: Callable[[List[str]], T],
        max: Union[int, None] = None
) -> List[T]:
    csv_file = open(file_path, "r")

    if has_header:
        csv_file.readline()

    result = []
    if max is not None:
        i = 0
        for line in csv_file:
            parts = list(line.strip().split(','))
            obj = transform(parts)
            result.append(obj)
            if i > max:
                break
            else:
                i += 1
    else:
        for line in csv_file:
            parts = list(line.strip().split(','))
            obj = transform(parts)
            result.append(obj)

    return result