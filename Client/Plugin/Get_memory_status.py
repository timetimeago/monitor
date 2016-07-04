# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import re,commands
def Get_memory_status():
    print 'Get memory running'
    val = commands.getoutput('free')
    Service = {
               'service':{}
               }
    # print ''.join(q.split(' '))
    data =  re.findall('^(.*?)$', val, re.MULTILINE)
    for i in range(1,4):
        L = []
        data[i] = data[i].split(' ')
        for val in data[i]:
            if val:
                L.append(val)
        data[i] =  L
        
    for i in range(1,4,2):
        Service['service'][data[i][0]] = {
                                                  'Total':data[i][1],
                                                  'Used':data[i][2],
                                                  'Free':data[i][3],
                                                  }
        Service['service'][data[2][1]] = {
                                          'Buffer':data[2][2],
                                          'Cached':data[2][3],
                                          }
    return Service['service']
