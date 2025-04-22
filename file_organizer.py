import os
import shutil

def organize_files(directory):
    # تعریف پوشه‌های مقصد بر اساس نوع فایل
    extensions = {
        'Images': ['.jpg', '.png', '.jpeg'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv'],
        'Others': []
    }
    
    # ایجاد پوشه‌ها اگه وجود ندارن
    for folder in extensions.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # مرور فایل‌های پوشه
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # پیدا کردن پسوند فایل
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            # انتقال فایل به پوشه مناسب
            for folder, exts in extensions.items():
                if file_ext in exts:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    print(f'Moved {filename} to {folder}')
                    moved = True
                    break
            # اگه پسوند ناشناخته بود، به Others بره
            if not moved and file_ext:
                shutil.move(file_path, os.path.join(directory, 'Others', filename))
                print(f'Moved {filename} to Others')

if __name__ == "__main__":
    # مسیر پوشه‌ای که می‌خوای مرتب کنی
    target_directory = "C:/Users/PARS/Desktop/TestFolder"  
    organize_files(target_directory)