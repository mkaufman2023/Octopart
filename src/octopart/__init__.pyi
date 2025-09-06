"""
src/octopart/__init__.pyi

Stub for `__init__.py`.
"""

__all__ = ["view", "all_categories", "suggested_filter_search"]

def view(data: list | dict) -> None: ...
def all_categories() -> list[dict]: ...
def suggested_filter_search(query: str) -> list[dict]: ...
