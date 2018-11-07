import os
import platform


def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        ips = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]

        print("Call Windows tasks")
    elif (sysstr == "Linux"):
        print("Call Linux tasks")
        ip = [a for a in os.popen('/sbin/route').readlines() if 'default' in a][0].split()[1]

    else:
        print("Other System tasks")
    print(ips)


UsePlatform()
