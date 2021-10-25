import platform
import os, subprocess

OS_Platform = platform.system()

print(f'It is a {OS_Platform} Platform')

if OS_Platform == "Windows":
    cmd = "java -version"
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    rc = sp.wait()
    print(f'Return code {rc}')
    o, e = sp.communicate()
    for each in e.splitlines():
        if 'version' in each:
            print(each.split()[2].strip('"'))
elif OS_Platform == "Linux":
    cmd = ["java", "-version"]
    sp = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    rc = sp.wait()
    print(f'Return code {rc}')
    o, e = sp.communicate()
    for each in o.splitlines():
        if 'version' in each:
            print(each.split()[2].strip('"'))
else:
    print("Invalid OS Platform")

# It is a Windows Platform
# Return code 0
# 1.8.0_281
