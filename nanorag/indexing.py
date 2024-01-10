# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_indexing.ipynb.

# %% auto 0
__all__ = ['context', 'store']

# %% ../nbs/06_indexing.ipynb 2
from .base import *
from .store import *
from .context import *
from .llm import *
from .loaders import *
from typing import Union, List, Dict, Tuple, Optional, Any
import numpy as np

# %% ../nbs/06_indexing.ipynb 3
#| eval: false
context = ModelContext()
context.set_default()
store = DocumentStore()
