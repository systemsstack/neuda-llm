"""A dict subclass that supports attribute style access.

Can probably be replaced by types.SimpleNamespace from Python 3.3
"""
from typing import Any
from typing import Dict
from typing import Self

class Struct(Dict[str, Any]):
    _allownew: bool = True
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def __iadd__(self, other: Struct) -> Self: ...
    def __add__(self, other: Struct) -> Struct: ...
    def __sub__(self, other: Struct) -> Struct: ...
    def __isub__(self, other: Struct) -> Self: ...
    def dict(self) -> Self: ...
    def copy(self) -> Self: ...
    def hasattr(self, key: str) -> bool: ...
    def allow_new_attr(self, allow: bool = True) -> None: ...
    def merge(
        self,
        __loc_data__: Dict[str, Any] | Struct | None = ...,
        __conflict_solve: Dict[str, Any] | None = ...,
        **kw: Any,
    ) -> Struct: ...
