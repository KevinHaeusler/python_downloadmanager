import os
import shutil
import datetime

# Set Download Folder and initialise Download Files
download_folder = r'C:\Users\kevin\Downloads'
download_files = os.listdir(download_folder)
downloading_file = ''
# Set Destination Folders
exe_folder = r'C:\Users\kevin\Downloads\EXE'
misc_folder = r'C:\Users\kevin\Downloads\MISCELLANEOUS'
pdf_folder = r'C:\Users\kevin\Downloads\PDF'
pictures_folder = r'C:\Users\kevin\Downloads\PICTURES'
videos_folder = r'C:\Users\kevin\Downloads\VIDEOS'
zip_folder = r'C:\Users\kevin\Downloads\ZIP'
# Exclude Destination Folders
excluded_folders = ["EXE", "MISCELLANEOUS", "PDF", "PICTURES", "VIDEOS", "ZIP"]
# Set Log File
log_file = r'D:\Scripts\Downloadmanager\LOG\downloadmanager.log'
# Set Date for Log File
now = datetime.datetime.now()
# Iterate through all Files in Download Directory
for file in download_files:
    f = open(log_file, "a")
    log_text = now.strftime("%Y-%m-%d %H:%M") + ": "
    if file not in excluded_folders:
        downloading_file = file + '.part'
        if downloading_file not in download_files:
            if file.endswith('.exe'):
                shutil.move(os.path.join(download_folder, file), os.path.join(exe_folder, file))
                log_text = log_text + "Moved " + file + " to " + exe_folder + "\n"
                f.write(log_text)
            else:
                if file.endswith('.pdf'):
                    shutil.move(os.path.join(download_folder, file), os.path.join(pdf_folder, file))
                    log_text = log_text + "Moved " + file + " to " + pdf_folder + "\n"
                    f.write(log_text)
                else:
                    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'):
                        shutil.move(os.path.join(download_folder, file), os.path.join(pictures_folder, file))
                        log_text = log_text + "Moved " + file + " to " + pictures_folder + "\n"
                        f.write(log_text)
                    else:
                        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv'):
                            shutil.move(os.path.join(download_folder, file), os.path.join(videos_folder, file))
                            log_text = log_text + "Moved " + file + " to " + videos_folder + "\n"
                            f.write(log_text)
                        else:
                            if file.endswith('.zip') or file.endswith('.7z') or file.endswith('.rar'):
                                shutil.move(os.path.join(download_folder, file), os.path.join(zip_folder, file))
                                log_text = log_text + "Moved " + file + " to " + zip_folder + "\n"
                                f.write(log_text)
                            else:
                                if file.endswith('.ini') or file.endswith('.part'):
                                    print("Ignoring ",file)
                                else:
                                    shutil.move(os.path.join(download_folder, file), os.path.join(misc_folder, file))
                                    log_text = log_text + "Moved " + file + " to " + misc_folder + "\n"
                                    f.write(log_text)

        f.close()