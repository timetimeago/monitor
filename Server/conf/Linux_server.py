# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import Monitor_service_Norm
#from The_func_of_Data import avg,hit,most

class Cpu(Monitor_service_Norm.Base_server_Norm):
    def __init__(self):
        super(Cpu,self).__init__()
        self.name = 'Monitor_Cpu'
        self.interval = 30
        self.plugin_name = 'Get_Cpu_status'
        self.trigger = {
                               'idle':{
                                       'func':'avg',
                                       'minuter':10,
                                       'warning':50,
                                       'critical':80,
                                       'type':'percent',
                                       },
                               'user':{
                                       },
                               'sys':{
                                      },
                               'wait':{
                                       'func':'hit',
                                       'minuter':10,
                                       'threshold':20,
                                       'warning':5,
                                       'critical':10
                                       },
                        }
    
class Memory(Monitor_service_Norm.Base_server_Norm):
    def __init__(self):
        super(Memory,self).__init__()
        self.name = 'Monitor_Memory'
        self.interval = 30
        self.plugin_name = 'Get_Memory_status'
        self.trigger = {
                               'Total':{
                                       'Memory',
                                       },
                               'used':{'func':'avg',
                                       'minuter':1,
                                       'warning':50,
                                       'critical':80,
                                       'type':'percent',       
                                       },
                        }
