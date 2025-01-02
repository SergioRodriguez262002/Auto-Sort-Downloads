#!/usr/bin/env python3
import time, os, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def autosort():
    mock_download_path = "/home/hp-laptop1/Desktop/mock_download"
    seen_folders = []
    files_no_folders = []

    test_moved_folders = []
    try:
        entries = os.scandir(mock_download_path)
        for entry in entries:
            if "." in entry.name :
                name, extention = entry.name.split(".")

                if extention in seen_folders:
                    full_dir = mock_download_path+"/"+extention
                    test_moved_folders.append((entry.path,full_dir))
                else:
                    files_no_folders.append(entry)

            else:
                if not entry.name in seen_folders:
                    seen_folders.append(entry.name)

        for entry in files_no_folders:
            if "." in entry.name:
                name, extention = entry.name.split(".")
                if extention in seen_folders:
                    full_dir = mock_download_path+"/"+extention
                    test_moved_folders.append((entry.path,full_dir))

                else:
                    seen_folders.append(extention)
                    os.mkdir(mock_download_path+"/"+extention)
                    full_dir = mock_download_path+"/"+extention
                    test_moved_folders.append((entry.path,full_dir))

        # # OPTIMIZE: for less for loops move during the above
        for entry  in test_moved_folders:
            shutil.move(entry[0],entry[1])


    finally:
        entries.close()


class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        # print(f"New file created: {event.src_path}")
        # add custom action
        autosort()

def watch_directory(directory):
    event_handler = WatcherHandler()
    observer = Observer()

    observer.schedule(event_handler, directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    download_directory = "/home/hp-laptop1/Desktop/mock_download"
    #print(f"Watching directory: {download_directory}")
    watch_directory(download_directory)
