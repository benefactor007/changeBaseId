# coding="utf-8"

import pexpect
import sys

ip = sys.argv[1]



def main():
    try:
        p1 = pexpect.spawn("telnet "+ ip, timeout=15, logfile=sys.stdout)
        # p1.expect("login:", timeout=15, logfile=sys.stdout)
        p1.expect("login:")
        p1.sendline("root")
        # p1.expect("Password", timeout=15, logfile=sys.stdout)
        p1.expect("Password")
        p1.sendline("root")
        p1.sendline("mount-read-write.sh")
        """Due to partition permissions of root changed, move the SetKey file from /var/tmp -> /tmp"""
        p1.sendline("chmod +x /tmp/tsd.persistence.client.mib3.app.SetKey")
        # p1.sendline("chmod +x /var/tmp/tsd.persistence.client.mib3.app.SetKey")
        #p1.sendline("chmod +x /var/tmp/tsd.persistence.client.mib3.app.InitPersistence")
        #p1.sendline("/var/tmp/tsd.persistence.client.mib3.app.InitPersistence")
        # p1.sendline("/var/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x80000008 --key 0x00  --val 0xe5")
        p1.sendline("/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x80000008 --key 0x00  --val 0xe5")
        # Set Hardware version >> X20
        # p1.sendline("/var/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF1A3  --val 0x583230")
        p1.sendline("/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF1A3  --val 0x583230")
        # Set Software version >> C420
        #p1.sendline("/var/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF189  --val 0x43343230")
        # Set PartNum >> 3GB035866A
        # p1.sendline("/var/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF187 --val 0x3347423033353836364120")
        # p1.sendline("/var/tmp/tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF191 --val 0x3347423033353836364120")
        p1.sendline("sync")
        p1.sendline("exit")
        p1.expect("Connection closed by foreign host")
        p1.expect(pexpect.EOF)
        print "\033[32m" + "PASS" + "\033[0m"  # print Green font

    except Exception:
        print "Something is going wrong!"


if __name__ == '__main__':
    main()
