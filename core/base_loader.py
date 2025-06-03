from abc import ABC, abstractmethod
import pandas as pd
schemas = {
    'datos': {
        'nombre': {'type': str, 'required': True},
        'edad': {'type': int, 'required': True}
    },
    'personas': {
        'nombre': {'type': str, 'required': True},
        'edad': {'type': int, 'required': True}
    }
}

class FileLoader(ABC):
    def __init__(self, filepath: str):
        self._filepath = filepath         # Encapsulamiento (atributo protegido)
        self._data = None                 # DataFrame que se cargará

    @abstractmethod
    def read(self) -> None:
        """Leer el archivo y cargar los datos en un DataFrame."""
        pass

    @abstractmethod
    def get_table_name(self) -> str:
        """Obtener el nombre de la tabla para guardar en la base de datos."""
        pass

    def get_data(self) -> pd.DataFrame:
        """Devolver los datos ya cargados."""
        return self._data

    def validate(self) -> bool:
     if self._data is None or self._data.empty:
        return False

    # Eliminar duplicados y filas completamente nulas
     self._data.drop_duplicates(inplace=True)
     self._data.dropna(how='all', inplace=True)

     table = self.get_table_name()

    # Validación por esquema si existe
     schema = schemas.get(table)
     if schema:
        for column, rules in schema.items():
            if rules.get("required") and self._data[column].isnull().any():
                print(f"❌ Columna obligatoria '{column}' tiene valores nulos.")
                return False
            if "type" in rules:
                # Checkea tipo en las filas no nulas
                valid = self._data[column].dropna().map(lambda x: isinstance(x, rules["type"])).all()
                if not valid:
                    print(f"❌ Columna '{column}' tiene tipos incorrectos. Se esperaba {rules['type'].__name__}")
                    return False
     return True

