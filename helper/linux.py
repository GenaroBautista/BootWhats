import os


class Linux:
    def get_disk_usage(self):
        return f"Disk status: \n\n{os.popen('df -h').read()}"
    
       def get_memory_usage(self):
           return f"Memory status: \n\n{os.popen('free -m').read()}"
       
       
    
