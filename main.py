import os
from core.csv_loader import CSVLoader
from core.json_loader import JSONLoader
from core.database import Database

def get_loader(filepath: str):
    if filepath.endswith('.csv'):
        return CSVLoader(filepath)
    elif filepath.endswith('.json'):
        return JSONLoader(filepath)
    else:
        return None

def main():
    db = Database()
    folder = "files"
    resultados = []

    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        loader = get_loader(filepath)

        if loader:
            loader.read()
            if loader.validate():
                db.save_data(loader.get_data(), loader.get_table_name())
                resultados.append((file, "✅ Cargado"))
            else:
                resultados.append((file, "❌ Falló la validación"))
        else:
            resultados.append((file, "⏩ Tipo de archivo no soportado"))

    print("\n📋 Resultado Final:")
    for file, status in resultados:
        print(f"{file}: {status}")

if __name__ == '__main__':
    main()
