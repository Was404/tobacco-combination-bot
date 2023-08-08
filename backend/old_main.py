import pandas as pd

sovpad_vkusi = pd.read_excel('data\TABAKI2.xlsx')
black_bern = pd.read_excel('data\BlackBern.xlsx')

print('## Сочетания вкусов табака фирмы BlackBern ##')
print('Введите первый вкус (ВЫБОР ИЗ НАЗВАНИЙ)')
first_obj = input()
print('Введите второй вкус (ВЫБОР ИЗ НАЗВАНИЙ)')
second_obj = input()
# ЗДЕСЬ ПОЛУЧАЕМ ВКУС(НАЗВАНИЕ СТОЛБЦА) ПО ЕЁ СОДЕРЖАНИЮ
try:
    name_of_col1 = black_bern.columns[black_bern.isin([first_obj]).any()][0] # [0] используется, чтобы выбрать первый элемент списка (если он есть)
    name_of_col2 = black_bern.columns[black_bern.isin([second_obj]).any()][0] 
    print(name_of_col1)
    print(name_of_col2)
except:
    print(f"\"{first_obj}\" или \"{second_obj}\" не найден в таблице")
# найти индекс первой строки с name_of_col1 в первом столбце
idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == name_of_col1].index[0]
# найти название первого столбца, содержащего name_of_col2
col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(name_of_col2)][0]
result = sovpad_vkusi.loc[idx, col_name]

print(f"Можно ли смешивать?\n Ответ: {result}")
