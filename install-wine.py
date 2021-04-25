import os
from elevate import elevate
listOCmds = [
    "echo Preparing for installation..."
    "echo **********"
    "dpkg --add-architecture i386",
    "echo Downloading keys..."
    "wget -nc \"https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/Debian_10/Release.key\"",
    "apt-key add Release.key",
    "rm Release.key",
    "wget -nc https://dl.winehq.org/wine-builds/Release.key",
    "apt-key add Release.key",
    "rm Release.key",
    "touch /etc/apt/sources.list.d/wine.list",
    "echo **********",
    "echo Writing wine.list at /etc/apt/sources.list.d/wine.list ...",
    "writeListFile",
    "echo **********",
    "echo Updating system...",
    "apt update",
    "echo **********",
    "echo Installing...",
    "apt install --install-recommends winehq-stable",
    "echo Installation finished"
]
if __name__ == "__main__":
    print("**********")
    print("Welcome to wine 6.0 installer")
    print("Created by 谦言谦语")
    print("**********")
    if os.getuid() != 0:
        elevate()
    for i in listOCmds:
        if i=="writeListFile":
            with open("/etc/apt/sources.list.d/wine.list",'w') as f:
                f.write("deb https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/Debian_10 ./")
                f.write("\n")
                f.write("deb https://dl.winehq.org/wine-builds/debian/ buster main")
                f.write("\n")
        else:
            os.system(i)
        print("**********")

