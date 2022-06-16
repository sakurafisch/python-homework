from functools import singledispatch
from typing import Optional

@singledispatch
def my_print(s: str, k: Optional[int] = None) -> None:
    if not k:
        print(s)
        return
    print(str(k) + ' ' + s)

@my_print.register(int)
def _(i: int) -> None:
    print(i * 2)

@my_print.register(float)
def _(s: float) -> None:
    print(s * 4)


def main() -> None:
    my_print("hello world")
    my_print("halo", 2)
    my_print(2)
    my_print(5.0)

if __name__ == '__main__':
    main()
