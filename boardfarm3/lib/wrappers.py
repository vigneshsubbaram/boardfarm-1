"""Boardfarm decorators module."""


from typing import Any, TypeVar

AnyClass = TypeVar("AnyClass")


def singleton(cls: type[AnyClass]) -> AnyClass:
    """Allow a class to become a decorator."""
    instances = {}

    def getinstance(*args: tuple, **kwargs: Any) -> AnyClass:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return getinstance  # type: ignore[return-value]
