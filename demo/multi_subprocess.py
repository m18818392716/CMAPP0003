import subprocess
from time import ctime
"""
这里需要使用subprocess模块，该模块可以创建新的进程，并且连接到进程的输入、输出、错误等管道信息，并且可以获取进程的返回值
场景
使用Python启动2台appium服务，端口配置如下：

Appium服务器端口：4723，bp端口为4724
Appium服务器端口：4725，bp端口为4726
说明：bp端口（ –bootstrap-port）是appium和设备之间通信的端口，如果不指定到时无法操作多台设备运行脚本
"""

def appium_start(host,port):
    # bp端口（ –bootstrap-port）是appium和设备之间通信的端口
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p '+ str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('../appiumlog/'+str(port)+'.log', 'a'), stderr=subprocess.STDOUT)

# if __name__ == '__main__':
#     host = '127.0.0.1'
#     port = 4723
#     appium_start(host,port)

# 多个appium服务启动
if __name__ == '__main__':
    host = '127.0.0.1'
    for i in range(2):
        port=4723+2*i
        appium_start(host,port)
        print("第 {} 个appium进程启动成功".format(i+1))

# 校验是否成功：
# 1.cmd中输入netstat -ano | findstr 端口号（4723）  ---查看appium进程端口号
# 2. 在appiumlog路径中生成4723.log日志文件
# 3、终止appium服务： taskkill -f -pid appium进程，如下：

