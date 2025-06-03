import pandas as pd
import os
from core.base_loader import FileLoader

class JSONLoader(FileLoader):
    def read(self) -> None:
        try:
            self._data = pd.read_json(self._filepath)
        except Exception as e:
            print(f"❌ Error al leer archivo JSON '{self._filepath}': {e}")
            self._data = None

    def get_table_name(self) -> str:
        return os.path.splitext(os.path.basename(self._filepath))[0].lower()
