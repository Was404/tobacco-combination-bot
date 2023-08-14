import pandas as pd
import os
from main import result
# This is file need for experiments and new features
path = 'backend\data\BlackBern.xlsx'
def find_all_names(path): #функция для поиска всех наименнований табака одного производителя
    #dataname = os.path.basename(path).replace(".xlsx", "") 
    dataname, _ = os.path.splitext(os.path.basename(path))
    black_bern = pd.read_excel('data\BlackBern.xlsx')
    print(black_bern[dataname]) #Выводим все вкусы данного производителя (В будущем можно передавать путь к производителю, который необходим)
find_all_names(path)

def result_for_user(result):
    k = 0
    for i in range(len(result)):
        if result[i] == 'Да':
            k += 1
        else:    
            k -= 1
    if k >= 2 :
        otvet = 'Смешать можно'        