from dataclasses import dataclass


@dataclass
class A:
    x: int


@dataclass
class B:
    x: int


a = A(x=1)
b = B(x=1)

a.x = 99  # what happens?
b.x = 99  # what happens?
d = {a: "hello"}  # what happens?
d = {b: "hello"}  # what happens?

{}
