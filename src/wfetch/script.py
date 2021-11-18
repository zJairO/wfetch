import os, socket, platform, subprocess, sys, ctypes, platform
from colorama import init
init()
from colorama import Fore, Back, Style

uname = platform.uname()

def asciiRet(self):
    print(Fore.BLUE+"                   .oodMMMMMMMMMMMMM"+Fore.GREEN+f" {self.user}"+Fore.WHITE+" @ "+Fore.GREEN+f"{self.name}")
    print(Fore.BLUE+"       ..oodMMM  MMMMMMMMMMMMMMMMMMM" +Fore.GREEN+f" Host"+Fore.WHITE+f": {self.host}")
    print(Fore.BLUE+" oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"+Fore.GREEN+ f" Os" +Fore.WHITE+f": {self.osn}")
    print(Fore.BLUE+" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM" +Fore.GREEN+f" Version"+Fore.WHITE+f": {self.version}")
    print(Fore.BLUE+" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"+Fore.GREEN+f" Uptime"+Fore.WHITE+f": {self.uptime}")
    print(Fore.BLUE+" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"+Fore.GREEN+" Architecture"+Fore.WHITE+": "+platform.architecture()[0])
    print(Fore.BLUE+" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM")#+Fore.GREEN+" Processor"+Fore.WHITE+f": {uname.processor}"
    print(" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM")
    print("""\n MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM""")



class Computer:
    def __init__(self, user, name, osn, host, version, uptime):
        self.user = user
        self.name = name
        self.osn = osn
        self.host = host
        self.version = version
        self.uptime = uptime

    

    def ascii(self):
        return asciiRet(self)
    

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

def main():
    print(win.ascii())

if __name__ == "__main__":
    main()

