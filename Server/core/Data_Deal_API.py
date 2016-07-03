# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
Data =  {'buffers/cache:': {'Buffer': '634780', 'Cached': '1271776'}, 'Swap:': {'Used': '0', 'Free': '2097144', 'Total': '2097144'}, 'Mem:': {'Used': '1547352', 'Free': '359204', 'Total': '1906556'}}
import RedisOperate
from Server.conf import Linux_server
r1 = RedisOperate.Redis_Instance()
r2 = Linux_server.Memory()
def Monitor_Memory(Client_IP,Data,Time,Flag):
    Total = Data['Mem:']['Total']
    Used  = Data['Mem:']['Used']
    key = '%s-Mem-%s'%(Client_IP,Time)
    val = (Total,Used)
#     print Total
    r1.Set(key, val)
    if Flag >= r2.trigger['used']['minuter']:
        r2.trigger['used']['func']()
    return True
def Monitor_Cpu(Client_IP,Data):
    pass
if __name__ == '__main__':
    Monitor_Memory('123', Data,'asd',20)