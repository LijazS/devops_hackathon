import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil
from pathlib import Path


class DeletionHandler(FileSystemEventHandler):
    def on_deleted(self, event):

        super().on_deleted(event)

    

        what = 'directory' if event.is_directory else 'file'
        print(f"[{time.ctime()}] Deleted: {what} at path: {event.src_path}")
        filepath = event.src_path
        spl = filepath.split("\\")
        filename = spl[len(spl)-1]
        try:
            shadow_path = os.path.join(path,".shadow",filename)
            recycle_path = os.path.join(path,"recycle_bin")
            meta = os.stat(shadow_path)
            shutil.copy(shadow_path,recycle_path)
            with open(os.path.join(path,"recycle_bin",f"metadata_{filename}"),"w") as f:
                f.write(str(meta))
            print("file copied from shadow folder to recycle with metadata")
        except Exception:
            print("file doesnt exist in shadow folder")



if __name__ == '__main__':
   
    path = Path.cwd() / "qn1"
    
    event_handler = DeletionHandler()
    observer = Observer()
    
   
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    print(f"Watching directory: {os.path.abspath(path)} for deletions...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer stopped by user.")
    observer.join()
