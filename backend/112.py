import pandas as pd
<<<<<<< HEAD
=======
#import string
sovpad_vkusi = pd.read_excel('backend\data\TABAKI2.xlsx')
black_bern = pd.read_excel('backend\data\BlackBern.xlsx')
>>>>>>> d49d9bad18b51d78740338744169542de84815f5

sovpad_vkusi = pd.read_excel('backend\data\TABAKI2.xlsx')
black_bern = pd.read_excel('backend\data\BlackBern.xlsx')
black_bern.drop_duplicates(keep = "last", inplace = True)

<<<<<<< HEAD
def result(msg):

    words_list = msg.split(", ")
    print(words_list)
    result = []
    name_of_col_list = []
    count = 0
    print("ｔｈｅ ｍｉｘｅｒ ｈａｓ ｓｔａｒｔｅｄ")
    for i in range(len(words_list[:-1:])):
=======
msg = "Irish cream, Basillic, Haribon, Pistachio ice snow"
#extracted_words = str.maketrans("", "", string.punctuation)
#msg = msg.translate(extracted_words)
words_list = msg.split(", ")
print(words_list)
result = []
name_of_col_list = []

for i in range(len(words_list[:-1:])):
    first = words_list[i]
    second = words_list[i+1]
    print("INPUT:", first, second)
    name_of_col1 = black_bern.columns[black_bern.isin([first]).any()][0]
    if i<1:
         name_of_col_list.append(name_of_col1)
    name_of_col2 = black_bern.columns[black_bern.isin([second]).any()][0]
    name_of_col_list.append(name_of_col2)
    print("OUTPUT:", name_of_col1, name_of_col2)
>>>>>>> d49d9bad18b51d78740338744169542de84815f5

            first = words_list[i]
            second = words_list[i+1]
            print("INPUT:", first, "|", second)

<<<<<<< HEAD
            name_of_col1 = black_bern.columns[black_bern.isin([first]).any()][0]
            while count == 1:
                name_of_col_list.append(name_of_col1)
            name_of_col2 = black_bern.columns[black_bern.isin([second]).any()][0]
            name_of_col_list.append(name_of_col2)
=======
    result.append(f"{first}'{name_of_col1}' + {second}'{name_of_col2}' = {sovpad_vkusi.loc[idx, col_name]}")

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
>>>>>>> d49d9bad18b51d78740338744169542de84815f5
            print("OUTPUT:", name_of_col1, name_of_col2)

            idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == name_of_col1].index[0]
            print("IDX:", idx)   
            col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(name_of_col2)][0] 
            print("COLNAME", col_name)

<<<<<<< HEAD
            result.append(sovpad_vkusi.loc[idx, col_name])
            count +=1

    if len(words_list) > 2:
        print("!Start mathing last!")
        last = words_list[-1]
            
        for i in reversed(range(len(words_list) -1)):
            if i == len(words_list) - 2:
                    continue
            pepa = words_list[i]
            print("INPUT:", last, "|", pepa)

            name_of_col1 = black_bern.columns[black_bern.isin([last]).any()][0]
            name_of_col2 = black_bern.columns[black_bern.isin([pepa]).any()][0]
            print("OUTPUT:", name_of_col1, name_of_col2)

            idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == name_of_col1].index[0]
            print("IDX:", idx)   
            col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(name_of_col2)][0]
            print("COLNAME", col_name)

            result.append(sovpad_vkusi.loc[idx, col_name])
        print("ｗｏｒｋ ｉｓ ｏｖｅｒ")
        print(name_of_col_list)
        
        return result

if __name__ == "__main__":
    print(result("Basillic, Mirinda, Cheesecake"))
=======
            result.append(f"{first}'{name_of_col1}' + {second}'{name_of_col2}' = {sovpad_vkusi.loc[idx, col_name]}")
              
print("Что можно смешивать?\n")
pd.set_option('display.max_colwidth', None)
result_series = pd.Series(result)
result_series.reset_index(drop=True)
result_series.index += 1
print(result_series)
#print(name_of_col_list)


>>>>>>> d49d9bad18b51d78740338744169542de84815f5
