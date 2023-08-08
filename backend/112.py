import pandas as pd
#import string
sovpad_vkusi = pd.read_excel('data\TABAKI2.xlsx')
black_bern = pd.read_excel('data\BlackBern.xlsx')

print("Кол-во столбцов ", black_bern.shape[1])
print("Кол-во столбцов TABAKI2", sovpad_vkusi.shape[1])

msg = "Irish cream, Basillic, Haribon, Pistachio ice snow"
#extracted_words = str.maketrans("", "", string.punctuation)
#msg = msg.translate(extracted_words)
words_list = msg.split(", ")
print(words_list)
result = []

for i in range(len(words_list[:-1:])):
    first = words_list[i]
    second = words_list[i+1]
    print("INPUT:", first, second)
    name_of_col1 = black_bern.columns[black_bern.isin([first]).any()][0]
    name_of_col2 = black_bern.columns[black_bern.isin([second]).any()][0]
    print("OUTPUT:", name_of_col1, name_of_col2)

    idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == name_of_col1].index[0]
    print("IDX:", idx)   
    col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(name_of_col2)][0] 
    print("COLNAME", col_name)

    result.append(sovpad_vkusi.loc[idx, col_name])
    print(result)

if len(words_list) > 2:
        print("!Start mathing last!")
        last = words_list[-1]
        
        for i in reversed(range(len(words_list) -1)):
            if i == len(words_list) - 2:
                continue
            pepa = words_list[i]
            print("INPUT:", last, pepa)

            name_of_col1 = black_bern.columns[black_bern.isin([last]).any()][0]
            name_of_col2 = black_bern.columns[black_bern.isin([pepa]).any()][0]
            print("OUTPUT:", name_of_col1, name_of_col2)

            idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == name_of_col1].index[0]
            print("IDX:", idx)   
            col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(name_of_col2)][0] 
            print("COLNAME", col_name)

            result.append(sovpad_vkusi.loc[idx, col_name])

print(result)
