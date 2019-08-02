from typing import Optional, Tuple

import numpy as np


class Generator(object):
    def __init__(
        self,
        shape: Tuple[int, ...],
        dtype: Optional[type] = np.float32,
        seed: Optional[int] = None,
    ):
        self.shape = shape
        self.dtype = dtype
        self._prng = np.random.RandomState(seed)

    def generate(self, seed: Optional[int]) -> np.ndarray:
        raise NotImplementedError