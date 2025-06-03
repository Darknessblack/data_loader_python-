from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
import pandas as pd

class Database:
    def __init__(self, db_url='sqlite:///data.db'):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def save_data(self, dataframe: pd.DataFrame, table_name: str):
        try:
            dataframe.to_sql(table_name, self.engine, if_exists='replace', index=False)
            print(f"✅ Datos guardados en tabla '{table_name}'")
        except Exception as e:
            print(f"❌ Error al guardar datos en tabla '{table_name}': {e}")
