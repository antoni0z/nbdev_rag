# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_utils.ipynb.

# %% auto 0
__all__ = ['hash_input']

# %% ../nbs/01_utils.ipynb 2
import hashlib

# %% ../nbs/01_utils.ipynb 3
def hash_input(input_data: str):
    hashed_input = hashlib.sha256(input_data.encode()).hexdigest()
    return hashed_input

