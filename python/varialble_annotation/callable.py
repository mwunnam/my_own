#!/usr/bin/python3
from typing import Callable

template = Callable[[int, int], int]

def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b


def mult(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    return a / b


def apply_all(func : template, a: int, b: int) -> int:
    return func(a, b)


if __name__ == "__main__":
    print(f"adding 10 and 20 is {apply_all(add, 10, 20)}")
    print(f"multiplyig 10 and 20 is {apply_all(mult, 10, 20)}")
    print(f"subtructing 20 from 10 is {apply_all(sub, 10, 20)}")
    print(f"dividing 10 by 20 is {apply_all(div, 10, 20)}")
