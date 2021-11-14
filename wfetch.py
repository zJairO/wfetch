import os, socket, platform, subprocess, sys, ctypes

class Computer:
    def __init__(self, user, name, osn, host, version, uptime):
        self.user = user
        self.name = name
        self.osn = osn
        self.host = host
        self.version = version
        self.uptime = uptime

    def ascii(self):
        return f"""
########@######## {self.user}@{self.name}
########@######## host    {self.host}
########@######## os      {self.osn}
@@@@@@@@@@@@@@@@@ version {self.version}
########@######## uptime  {self.uptime}
########@########
########@######## 
"""

def getHost():
    command = "wmic baseboard get product"
    output = subprocess.check_output(command, shell=True).decode()
    output = output.replace('Product', '').strip()
    return output

def getUpTime():
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)

    return f"{hour:01}h {mins:01}m"

    

win = Computer(os.getlogin(), socket.gethostname(), platform.system() + " " + platform.release(), getHost(), sys.getwindowsversion().build, getUpTime())

print(win.ascii())