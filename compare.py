import os # бибилиотека для работы с файлами
import sys # для считывания аргументов скрипта

def compare(file1_name, file2_name):    # расстояние Левенштейна
    """
    считываем файлы для сравнения
    """
    if not os.path.exists(file1_name):
        print("Файла ", file1_name, " не существует.")
    else:
        file1 = open(file1_name, 'r', encoding='UTF-8')
        array1 = file1.readlines()

    if not os.path.exists(file2_name):
        print("Файла ", file2_name, " не существует.")
    else:
        file2 = open(file2_name, 'r', encoding='UTF-8')
        array2 = file2.readlines()

    """
      Рассчитываем расстояние Левенштейна
    """
    len1, len2 = len(array1), len(array2)
    if len1 > len2:
        array1, array2 = array2, array1
        len1, len2 = len2, len1

    current_row = range(len1 + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, len2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len1
        for j in range(1, len1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if array1[j - 1] != array2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return round(1-current_row[len1]/len2, 3)

def get_files(input, output):           # процедура считывания файлов для сравнения
    if os.path.exists(input) and os.path.exists(output):
        file_names = open(input, 'r', encoding='UTF-8')
        file_out = open(output, 'a', encoding='UTF-8')
        file_out.truncate(0)
        """
        идём по парам файлов
        """
        files_for_comp=[]
        for f in file_names:
            files_for_comp = f.split()
            """
            получаем значение процента и записываем его в файл
            """
            file_out.write(str(compare(files_for_comp[0], files_for_comp[1]))+ '\n')
        file_names.close()
        file_out.close()
    else:
        print("Аргументы скрипта некорректны")

"""
Обрабатываем входные файлы.
"""
get_files(sys.argv[1], sys.argv[2])