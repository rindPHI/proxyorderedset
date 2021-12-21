# (Proxy-) OrderedSet

A simple implementation of ordered sets as a proxy to Python's standard dict class.

The implementation is based on the idea to take a `base` iterable and create a dict using `dict.fromkeys(base)`.
Keys are unique, and in newer versions of Python, the order is kept; values are `None` and ignored.

This package has no external dependencies. The OrderedSet class overwrites all `set` methods.

## Example

```python
from orderedset import OrderedSet

s: OrderedSet[int] = OrderedSet([3, 1, 4, 1])
list(s)  # yields [3, 1, 4]
```

## Build

Run `python3 setup.py sdist`. You find the file `proxyorderedset-0.1.tar.gz` in the `dist/` directory. Install
it, for example, with `pip3 install proxyorderedset-0.1.tar.gz`.