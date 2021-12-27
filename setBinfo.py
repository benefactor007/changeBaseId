# coding="utf-8"

import os

def main():
    #os.system("python2.7 testPexpect.py tsd.persistence.client.mib3.app.InitPersistence 192.168.1.4")
    os.system("python2.7 testPexpect.py tsd.persistence.client.mib3.app.SetKey 192.168.1.4")
    os.system("python2.7 baseInfoPexpect.py 192.168.1.4")


if __name__=='__main__':
    main()
