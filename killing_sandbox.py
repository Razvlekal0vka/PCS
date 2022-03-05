import subprocess
import time

import psutil


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    gone, still_alive = psutil.wait_procs(children, timeout=5)
    if including_parent:
        parent.kill()
        parent.wait(5)


process = subprocess.Popen(['python.exe', "start_box.py"])

time.sleep(10)

process.kill()

PROCNAME = "Bandicam_Portable.exe"
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        kill_proc_tree(proc.pid)
        break
