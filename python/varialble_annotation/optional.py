#!/usr/bin/python3
from typing import Optional

def greeting(name: Optional[str]) -> str:
    if name is None:
        return "Hello stranger"
    else:
        return f"hello {name}"


if __name__ == "__main__":
    print(greeting("Michael"))
    print(greeting(None))
