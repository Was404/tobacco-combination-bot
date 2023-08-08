import pandas as pd
import os

# Указываем папку, в которой будем искать файлы
folder_path = 'data'

# Получаем список всех файлов в указанной папке
file_list = os.listdir(folder_path)

# Проходим по каждому файлу в списке
for file_name in file_list:
    # Проверяем, является ли файл XLSX файлом
    if file_name.endswith('.xlsx'):
        # Составляем полный путь к файлу
        file_path = os.path.join(folder_path, file_name)
        
        # Чтение XLSX файла в pandas DataFrame
        data = pd.read_excel(file_path)
        
        # Составляем полный путь для сохранения CSV файла
        csv_file_path = os.path.join(folder_path, file_name.replace('.xlsx', '.csv'))
        
        # Конвертация в CSV и сохранение
        data.to_csv(csv_file_path, index=False, encoding='utf-8')
        print("Convertation DONE!")
        