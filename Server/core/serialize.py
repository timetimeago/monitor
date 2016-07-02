# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import pickle,RedisOperate
from All_host_were_Monitored import Monitor_group

def Get_Client_Request(client_ip):
    Service = {
           'service':{}
           }
    Service_List = []
    for group in Monitor_group:
        if client_ip in group.host:
            Service_List.extend(group.Monitor_mod.keys())
    Service_List = set(Service_List)
    for service in Service_List:
        service = service()
        Service['service'][service.name] = [
                                            service.plugin_name,
                                            service.interval,
                                            ]
    return Service

def Flush_IP_conf_to_redis():
    r1 = RedisOperate.Redis_Instance()
    host_ip = []
    for group in Monitor_group:
        host_ip.extend(group.host)
    host_ip = set(host_ip)
    for Each in host_ip:
        key = 'Client_Config::%s'%Each
        r1.Set(key, pickle.dumps(Get_Client_Request(Each)))
    return True
def Get_data_from_redis():
    r2 = RedisOperate.Redis_Instance()
    
if __name__ == '__main__':
    Flush_IP_conf_to_redis()