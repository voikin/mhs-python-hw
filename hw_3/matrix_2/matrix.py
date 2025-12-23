import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

from .mixins import SerializationMixin, PrettyPrintMixin, PropertyMixin


class Matrix(
    NDArrayOperatorsMixin, SerializationMixin, PrettyPrintMixin, PropertyMixin
):
    def __init__(self, data):
        self._data = data.tolist()
        self._update_dimensions()

    def _update_dimensions(self):
        self._rows = len(self._data) if self._data else 0
        self._cols = len(self._data[0]) if self._rows > 0 and self._data[0] else 0

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(
            np.asarray(x._data if isinstance(x, Matrix) else x) for x in inputs
        )
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if isinstance(result, np.ndarray):
            return Matrix(result)
        return result

    def __array__(self, dtype=None):
        return np.asarray(self._data, dtype=dtype)
