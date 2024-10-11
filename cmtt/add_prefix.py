# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data_dir = 'D://Research//Data//Cell//CellTracking//DIC-C2DH-HeLa//mask'

    dir_names = os.listdir(data_dir)
    for dir_name in dir_names:
        small_dir = os.path.join(data_dir, dir_name)
        file_list = os.listdir(small_dir)
        for file_name in file_list:
            old_name = os.path.join(small_dir, file_name)
            new_name = old_name.replace('man_seg', 't')
            #new_name = os.path.join(small_dir, dir_name+'_'+file_name)
            os.rename(old_name, new_name)
