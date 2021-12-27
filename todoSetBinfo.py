# coding="utf-8"

import os
import sys




def getCurWorkDir():
    res = os.popen("echo `pwd`")
    return res.read().strip()


def checkFileExist(str):
    return os.path.exists(str)

def greenFont(str):
    return "\033[32m" + str + "\033[0m"

def main():
    serialNum = sys.argv[1]
    print "The serial num is", serialNum
    logDir = "ListOfSetBaseId"
    loc = getCurWorkDir() + '/' + logDir
    while True:
        if checkFileExist(loc) == False:
            os.system("mkdir "+ loc )
            print greenFont(loc + ' has been created')
        else:
            print getCurWorkDir() + '/' + logDir
            os.system("python2.7 setBinfo.py |tee -a "+getCurWorkDir() + '/' + logDir+ '/' + serialNum +'.txt')
            break


if __name__=='__main__':
    main()