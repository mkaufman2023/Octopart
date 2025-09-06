"""
# octopart
Reverse-engineered API for [Octopart](https://octopart.com/).

## Installation/Updating
- `pip install "git+https://github.com/mkaufman2023/Octopart.git@main"`
- `pip install --upgrade "git+https://github.com/mkaufman2023/Octopart.git@main"`

## Basic Usage
- *Importing the library*
```python
import octopart
```
- *Getting ...*
```python

```
- *Getting ...*
```python

```
"""
from ._utils import view
__version__ = "0.0.5"


def all_categories() -> list[dict]:
    from ._utils import request
    payload = {
        "operationName": "AllCategories",
        "query": "query AllCategories {\n  categories {\n    id\n    name\n    path\n    children {\n      id\n      name\n      path\n    }\n  }\n}",
    }
    response = request(payload)
    raw_data = response.json()["data"]["categories"]
    return raw_data


def suggested_filter_search(query: str) -> list[dict]:
    from ._utils import request
    payload = {
        "query": "query SuggestedFilterSearch($filters: Map, $q: String, $country: String!, $currency: String!, $limit: Int) {\n  search(\n    q: $q\n    filters: $filters\n    country: $country\n    currency: $currency\n    limit: $limit\n  ) {\n    results {\n      part {\n        id\n      }\n    }\n    all_filters {\n      id\n      group\n      name\n      shortname\n    }\n    suggested_filters {\n      shortname\n    }\n    specs_view_attribute_groups {\n      attributes {\n        id\n        name\n        shortname\n        group\n      }\n    }\n  }\n}",
        "variables": {
            "q": query,
            "filters": {
                "category_id": [
                    ""
                ]
            },
            "country": "US",
            "currency": "USD",
            "limit": 20
        },
        "operationName": "SuggestedFilterSearch"
    }
    response = request(payload)
    raw_data = response.json()["data"]["search"]
    return raw_data


