import pandas as pd
import sys
from app.database import engine

excel_file = "export_logistics_db.xlsx"

try:
    dfs = pd.read_excel(excel_file, sheet_name=None)
except FileNotFoundError:
    print(f"Ошибка: Файл {excel_file} не найден в корне проекта.")
    sys.exit(1)

for table_name, df in dfs.items():
    if not df.empty:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Таблица '{table_name}' загружена ({len(df)} записей)")
    else:
        print(f"️ Таблица '{table_name}' пуста в Excel файле")

print("Загрузка данных в базу завершена!")