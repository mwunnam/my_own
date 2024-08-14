#!/usr/bin/python3
from typing import Callable, Optional

greeter = Callable[[], str]


def say_hello():
    return "Hello dear friend"


def greeting(greeter: Optional[greeter]) -> str:
    if greeter:
        return greeter

    else:
        return "Sorry you can not be greeted"


if __name__ == "__main__":
    print(f"{say_hello()}")
    print(f"{greeting(None)}")
