# coding=utf-8
import sys
import pexpect
import re

# print '参数个数为:', len(sys.argv), '个参数。'
# print '参数列表:', str(sys.argv)
#

fileName = sys.argv[1]
tAddress = sys.argv[2]  # Target address

print fileName
print tAddress
#
# timeout = 60
#
fileAddress = "./" + fileName
# HUAddress = ip

tAddressType = ""


# HUAddress = 'root@' + ip + ":/var/tmp/"

def addressType(address):
    global tAddressType
    p1 = re.match(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}", address)
    if p1 != None:
        print "It was matching the HU's IP address:", p1.group()
        # ipAddress = 'root@' + address + ":/var/tmp/"  # root@192.168.1.4:/var/tmp/
        ipAddress = 'root@' + address + ":/tmp/"  # root@192.168.1.4:/var/tmp/
        tAddressType = "ip"
        return ipAddress
    else:
        p2 = re.match(r"/\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)", address)
        if p2 != None:
            print  "It was matching Linux's work directory:", p2.group()
            pwd = address
            tAddressType = "wd"
            return pwd
        else:
            print "the Address is wrong!!"
            return False


# print "scp " + fileAddress + " " + HUAddress

# dark blue


def main():
    global tAddressType
    # print "scp " + fileAddress + " " + addressType(tAddress)
    # print tAddressType
    p1 = pexpect.spawn("scp " + fileAddress + " " + addressType(tAddress), timeout=15, logfile=sys.stdout)
    try:
        if tAddressType == "ip":
            # print "root@" + tAddress + "'s password:"
            # print "Over here"
            p1.expect("root@" + tAddress + "'s password:")
            # print "Over here"
            p1.send("root\r")
        p1.expect(pexpect.EOF)
        # 运行该脚本后，你会发现其实 log.txt 是空的，没有记录 ls -l 命令的内容，原因是没有调用 send 或 read_nonblocking，真正的内容没有被 flush 到 log 中。如果在
        # fout.close() 之前加上 p.expect(pexpect.EOF)，log.txt 才会有 ls -l 命令的内容。
        # p1.logfile.close()
        print "\033[32m" + "PASS" + "\033[0m"  # print Green font
    except Exception:
        print "Something is going wrong, no match was found"


if __name__ == '__main__':
    main()

# p1 = pexpect.spawn("spawn scp "+ fileAddress +" " + HUAddress)
# p1.expect("root@$ip's password:", timeout=30, logfile=sys.stdout)
# p1.sendline("root")
# p1.expect(pexpect.EOF)

# child = pexpect.spawn("./run1.sh")
# try:
#     child.expect('password for jpcc', timeout=5)
# except Exception:
#     print "Timeout! There is no match"
#
#
# child.logfile = sys.stdout
# print child.logfile
# result = child.before + child.after
# print result
# child.sendline('jpcc')
# child.sendline('jiahao Wu')
# child.expect(pexpect.EOF)
#
# result = child.before
#
# print result

"""
#!/usr/bin/expect

set ip [lindex $argv 0]
set file [lindex $argv 1]

spawn scp ./$file root@$ip:/var/tmp/
set timeout 60
set pass 1
set goto state1
while {1} {
    switch -exact -- $goto {

        state1 {
             expect {
                timeout { send_user "\nFAILED\n"; set pass 0; set goto default }
                "root@$ip's password:"
             }

             send "root\r"
	     interact
             if {$pass == 1} {
                    set goto default
             }
        }

        default {
            if {$pass == 1} {
              send_user "\033\[0;32m\nPASS\033\[0m\n"
            } else {
              send_user "\033\[01;31m\nFAIL\033\[0m\n"; exit1
            }
            exit 1
        }
    }
}
"""
