import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, server_url, base_directory):
        self.server_url = server_url
        self.base_directory = base_directory

    def on_modified(self, event):
        if not event.is_directory:
            self.upload_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.upload_file(event.src_path)

    def upload_file(self, file_path):
        relative_path = os.path.relpath(file_path, self.base_directory)
        with open(file_path, 'rb') as f:
            files = {'fileToUpload[]': (relative_path, f)}
            response = requests.post(self.server_url, files=files)
            if response.status_code == 200:
                print(f"File '{relative_path}' uploaded successfully.")
            else:
                print(f"Failed to upload '{relative_path}'. Status code: {response.status_code}")

def start_watching(directory_to_watch, server_url):
    event_handler = FileEventHandler(server_url, directory_to_watch)
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=True)
    observer.start()
    print(f"Started watching directory: {directory_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    directory_to_watch = "path/to/your/folder"  # Update this path
    server_url = "http://yourserver.com/upload.php"  # Update this URL
    start_watching(directory_to_watch, server_url)
