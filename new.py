import os
os.system("clear")
green="\033[0;32m"        # Green
cyan  = "\033[96m"
yellow = '\33[93m'
print(green+"""
  _______        _____ _____  _____ ______ 
 |__   __|/\    / ____|  __ \|_   _|  ____|
    | |  /  \  | (___ | |__) | | | | |__   
    | | / /\ \  \___ \|  _  /  | | |  __|  
    | |/ ____ \ ____) | | \ \ _| |_| |     
    |_/_/    \_\_____/|_|  \_\_____|_|     
                                           
                                           """)

print (cyan+"\t\t       	Version : 1.0 ")
print (yellow+'***********************************************************')
os.system("apt update -y")
os.system("apt upgrade -y")
os.system("pip install requests")
os.system("pkg install python -y")
os.system("pkg install python2 -y")
os.system("pkg install php -y")
os.system("pkg install ruby -y")
