import shutil
import os

def clean_desktop():
    print('Beginning desktop cleaning...')
    
    desktop_dir_path = '/Users/sarahsantacruz/Desktop'
    desktop_folder_dir_path = '/Users/sarahsantacruz/desktop-folder'
    all_desktop_files = os.listdir(desktop_dir_path)

    if not os.path.exists(desktop_folder_dir_path):
        os.mkdir(desktop_folder_dir_path)

    for f in all_desktop_files:
        shutil.move(desktop_dir_path + '/' + f, desktop_folder_dir_path + '/' + f)

    print(f'{len(all_desktop_files)} desktop files have been moved.')

clean_desktop()