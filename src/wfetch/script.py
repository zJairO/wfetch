import os, socket, platform, subprocess, sys, ctypes
from colorama import Fore

class Computer:
    def __init__(self, user, name, osn, host, version, uptime):
        self.user = user
        self.name = name
        self.osn = osn
        self.host = host
        self.version = version
        self.uptime = uptime

    def ascii(self):
        txt = "\n"
        txt += Fore.BLUE + "########   " + Fore.CYAN + "########" + "    " + Fore.BLUE + f"{self.user}" + Fore.WHITE + "@" + Fore.CYAN + f"{self.name}" + "\n"
        txt += Fore.BLUE + "########   " + Fore.CYAN + "########" + "    " + Fore.BLUE + "host    " + Fore.WHITE + f"{self.host}" + "\n"
        txt += Fore.BLUE + "########   " + Fore.CYAN + "########" + "    " + Fore.BLUE + "os      " + Fore.WHITE + f"{self.osn}" + "\n"
        txt += Fore.BLUE + "########   " + Fore.CYAN + "########" + "    " + Fore.BLUE + "version " + Fore.WHITE + f"{self.version}" + "\n"
        txt += "                       " + Fore.BLUE + "uptime  " + Fore.WHITE + f"{self.uptime}" + "\n"
        txt += Fore.LIGHTBLUE_EX + "########   " + Fore.BLUE + "########" + "\n"
        txt += Fore.LIGHTBLUE_EX + "########   " + Fore.BLUE + "########" + "\n"
        txt += Fore.LIGHTBLUE_EX + "########   " + Fore.BLUE + "########" + "\n"
        txt += Fore.LIGHTBLUE_EX + "########   " + Fore.BLUE + "########" + "\n"
        return txt
        

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