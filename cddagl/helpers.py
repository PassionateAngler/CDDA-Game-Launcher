import psutil

def get_ui_locale():
    return None

def process_id_from_path(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    pids = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           if processName.lower() in proc.exe().lower() :
               pids.append(proc.pid)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    if len(pids):
        return pids[0]
    else:
        return None