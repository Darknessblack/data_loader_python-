import pandas as pd
import os
from core.base_loader import FileLoader

class CSVLoader(FileLoader):
    def read(self) -> None:
        try:
            self._data = pd.read_csv(self._filepath)
        except Exception as e:
            print(f"❌ Error al leer archivo CSV '{self._filepath}': {e}")
            self._data = None

    def get_table_name(self) -> str:
        # Nombre de tabla sin extensión ni carpeta
        return os.path.splitext(os.path.basename(self._filepath))[0].lower()
