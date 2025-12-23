from matrix_1 import Matrix as BaseMatrix

from .mixins import HashMixin, CacheMixin


class Matrix(BaseMatrix, HashMixin, CacheMixin):
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False

        self_data = self.data if isinstance(self.data, list) else self.data.tolist()
        other_data = other.data if isinstance(other.data, list) else other.data.tolist()

        return self_data == other_data

    def __hash__(self):
        return super().__hash__()

    def __matmul__(self, other):
        cache_key = (hash(self), hash(other))

        if self.is_cached(cache_key):
            return self.get_from_cache(cache_key)

        result = super().__matmul__(other)
        cached_result = Matrix(result.data)
        self.put_to_cache(cache_key, cached_result)

        return cached_result
