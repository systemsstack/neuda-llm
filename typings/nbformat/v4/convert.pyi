from typing import Any

from _typeshed import Incomplete

from .nbbase import (
    NotebookNode as NotebookNode,
    nbformat as nbformat,
    nbformat_minor as nbformat_minor,
)

def upgrade(nb: NotebookNode, from_version: Incomplete | None = ..., from_minor: Incomplete | None = ...) -> Any: ...
def upgrade_cell(cell: NotebookNode) -> Any: ...
def downgrade_cell(cell: NotebookNode) -> Any: ...
def to_mime_key(d: Any) -> Any: ...
def from_mime_key(d: Any) -> Any: ...
def upgrade_output(output: Any) -> Any: ...
def downgrade_output(output: Any) -> Any: ...
def upgrade_outputs(outputs: Any) -> Any: ...
def downgrade_outputs(outputs: Any) -> Any: ...
def downgrade(nb: NotebookNode) -> Any: ...
