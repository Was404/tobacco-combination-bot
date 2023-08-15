import pandas as pd
import os
# This is file need for experiments and new features
path = 'backend\data\BlackBern.xlsx'

def find_all_names(): #функция для поиска всех наименнований табака одного производителя
    #dataname = os.path.basename(path).replace(".xlsx", "") 
    dataname, _ = os.path.splitext(os.path.basename(path))
    black_bern = pd.read_excel('backend\data\BlackBern.xlsx')
    result = black_bern[dataname] #Выводим все вкусы данного производителя (В будущем можно передавать путь к производителю, который необходим)
    return result

def ManufacorChoice():
    folder_path = "backend\data"  # указать путь к папке 
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

ManufacorChoice()
        