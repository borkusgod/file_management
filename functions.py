# functions for moving/copying files

import shutil


def move_files(old_d, to_d):
    from_path = old_d
    to_path = new_d
    shutil.move(old_d, new_d)
    print(f'file\n {old_d} \nwas moved to \n{new_d}')


def copy_files():
    pass


