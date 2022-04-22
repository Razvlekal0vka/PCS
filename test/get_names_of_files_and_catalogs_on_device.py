import os


def get_paths_of_all_files_on_device(start_path):
    # Обойти дерево каталогов и распечатать имена каталогов и файлов

    # Если в os.walk() указать '.', то будут выведены все файлы и директории в текущем дереве каталогов
    for dirpath, dirnames, files in os.walk(start_path):
        print(f'FOUND DIRECTORY: {dirpath}')
        for file_name in files:
            print(file_name)


get_paths_of_all_files_on_device('C:/')  # стартовая папка поиска 'C:/'
