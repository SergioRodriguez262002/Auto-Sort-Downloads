import os, shutil

if __name__ == "__main__":

    download_dir = "/home/hp-laptop1/Desktop/mock_download"
    entries = os.scandir(download_dir)
    for entry in entries:
        if entry.is_dir():
            print("Directory "+entry.name)
        else:
            print("File "+entry.name)
