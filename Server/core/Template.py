# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
from Server.conf import Linux_server

class Base_Template(object):
    def __init__(self):
        self.host = []
        self.name = ''
        self.group_name = ''
        self.Monitor_mod = [
                            ]

class Linux_Monitor_Template(Base_Template):
    def __init__(self):
        super(Linux_Monitor_Template,self).__init__()
        self.name = 'Linux_Monitor_Template'
        self.Monitor_mod = [
                            Linux_server.Cpu,
                            Linux_server.Memory,
                            ]