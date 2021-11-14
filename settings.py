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