# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import Global_Path
import Template
from conf import Linux_server
h1 = Template.Linux_Monitor_Template()
h1.host = ['127.0.0.1','127.0.0.1']
#h1.Monitor_mod[Linux_server.Cpu] = 90
Monitor_group = [ h1 ,]




if __name__ == '__main__':
    for service,value in h1.Monitor_mod.iteritems():
        service = service()
        service.interval = value
        print service.interval,service.plugin_name
