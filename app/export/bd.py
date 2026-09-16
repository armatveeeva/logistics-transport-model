import pandas as pd
import sys
from app.database import engine

tables = [
    'basin', 'port', 'operator', 'service_type', 'container_line',
    'container_turnover', 'cargo', 'incident', 'risk'
]

print("Начинается экспорт данных в Excel...")

sheets_created = 0

with pd.ExcelWriter("export_logistics_db.xlsx", engine='openpyxl') as writer:
    for table in tables:
        try:
            query = f"SELECT * FROM {table}"
            df = pd.read_sql(query, engine)

            if not df.empty:
                df.to_excel(writer, sheet_name=table, index=False)
                print(f"Таблица '{table}' экспортирована ({len(df)} записей)")
                sheets_created += 1
            else:
                print(f"Таблица '{table}' пуста, пропускаем")

        except Exception as e:
            print(f"Ошибка при экспорте таблицы '{table}': {e}")

if sheets_created == 0:
    print("\nКРИТИЧЕСКАЯ ОШИБКА: Не удалось экспортировать ни одной таблицы.")
    sys.exit(1)
else:
    print(f"\nВыгрузка завершена! Успешно создано листов: {sheets_created}")