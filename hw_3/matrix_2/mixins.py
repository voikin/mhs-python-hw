import json
import pickle
from pathlib import Path


class SerializationMixin:
    def save_to_file(self, filepath: str, format: str = "json"):
        data = {
            "data": self.data if hasattr(self, "data") else None,
            "rows": self.rows if hasattr(self, "rows") else None,
            "cols": self.cols if hasattr(self, "cols") else None,
        }

        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)

        if format == "json":
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        elif format == "pickle":
            with open(path, "wb") as f:
                pickle.dump(self, f)
        else:
            raise ValueError(f"Неподдерживаемый формат: {format}")


class PrettyPrintMixin:
    def __str__(self):
        rows_str = []
        for row in self.data:
            row_str = "  ".join(f"{val:>6}" for val in row)
            rows_str.append(f"▌ {row_str} ▐")

        header = "▛" + "▀" * (len(rows_str[0]) - 2) + "▜" if rows_str else "▛▜"
        footer = "▙" + "▄" * (len(rows_str[0]) - 2) + "▟" if rows_str else "▙▟"

        return "\n".join([header] + rows_str + [footer])


class PropertyMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        if hasattr(self, "_update_dimensions"):
            self._update_dimensions()

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, value):
        self._cols = value
