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
        