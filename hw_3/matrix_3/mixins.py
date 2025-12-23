class HashMixin:
    """
    hash = сумма всех элементов * rows
    """

    def __hash__(self):
        if not hasattr(self, "data") or self.data is None or len(self.data) == 0:
            return 0

        total_sum = sum(sum(row) for row in self.data)
        hash_value = total_sum * self.rows

        return int(hash_value)


class CacheMixin:
    _cache = {}

    def get_from_cache(cls, key):
        return cls._cache.get(key)

    def put_to_cache(cls, key, value):
        cls._cache[key] = value

    def is_cached(cls, key):
        return key in cls._cache
