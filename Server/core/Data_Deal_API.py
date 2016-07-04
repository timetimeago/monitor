# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
#Data =  {'buffers/cache:': {'Buffer': '634780', 'Cached': '1271776'}, 'Swap:': {'Used': '0', 'Free': '2097144', 'Total': '2097144'}, 'Mem:': {'Used': '1547352', 'Free': '359204', 'Total': '1906556'}}
import RedisOperate,serialize,Global_Path
from conf import Linux_server
from conf import The_func_of_Data
r1 = RedisOperate.Redis_Instance()
def Monitor_Memory(Client_IP,Data,Time,Time1):
    temp1 = {}
    temp1 = serialize.Get_Client_Request(Client_IP)
    for val in temp1.values():
        func = val['Monitor_Memory'][3]['used']['func']
        Func = getattr(The_func_of_Data,func)
        minuter = val['Monitor_Memory'][3]['used']['minuter']
    
    Total = Data['Mem:']['Total']
    Used  = Data['Mem:']['Used']
    key = '%s-Mem-%s'%(Client_IP,Time)
    val = (Total,Used)
#     print Total
    r1.Set(key, val)
    Flag = (Time - Time1)/60
    if Flag >= minuter:
        Func()
        return Time
    return Time1
def Monitor_Cpu(Client_IP,Data):
    pass
if __name__ == '__main__':
    Monitor_Memory('123', Data,'asd',20)
