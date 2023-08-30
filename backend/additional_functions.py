import pandas as pd
import os

# This is file need for experiments and new features
path = 'backend/data/'

selected_variabl = ""

def handle_variable2(vare):
    global selected_variabl
    selected_variabl = vare

def find_all_names(): #функция для поиска всех наименнований табака одного производителя
    #dataname = os.path.basename(path).replace(".xlsx", "")
    if selected_variabl != "":
        path = 'backend/data/' + selected_variabl
    else:
        path = 'backend/data/BlackBern.xlsx' # Ничего не выбрали? Вернулись к экземпляру по умолчанию
    print(path)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_info_columns', 0)
    dataname, _ = os.path.splitext(os.path.basename(path)) # !!ВАЖНО!! ДОЛЖЕН БЫТЬ СТОЛБИК С ТАКИМ ЖЕ ИМЕНЕМ КАК ИМЯ ФАЙЛА  !!!
    black_bern = pd.read_excel(path)
    result = black_bern[dataname].dropna() #Выводим все вкусы данного производителя 
    return result

def ManufacorChoice(): #поиск всех exel файлов от производителей в data
    folder_path = "backend/data"  # указать путь к папке 
    excel_file = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xlsx") and file_name != "TABAKI2.xlsx":
            excel_file.append(file_name)
            
    if excel_file is not None:
        print("Найден файл:", excel_file)
        return excel_file
    else:
        print("Файл не найден")
        return excel_file


        