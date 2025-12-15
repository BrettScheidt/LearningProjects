#Create a push pull files from SFTP
import paramiko  #can install via - pip install paramiko

sshclient = paramkio.SSHClient() #Sets up an SSH Client for us to use


#Pulls all the varaibles from a config file specified from user then triggers the 
def varCreation(file1):
    with open(file1, 'r') as f:
        for line in f:
            x=line.strip()
            if("username" in x.lower()):
                username = x.split(":",1)[1]
            if("password" in x.lower()):
                password = x.split(":",1)[1]
            if("host" in x.lower()):
                host = x.split(":",1)[1]
            if("port" in x.lower()):
                port = x.split(":",1)[1]
            if("file:" in x.lower()):
                file = x.split(":",1)[1]
            if("path" in x.lower()):
                filepath = x.split(":",1)[1]
    sshLogin(host,port,username,password,file,filepath)

def sshLogin(host,port,user,password,file,filepath):
    try:
        sshclient.connect(host,port,user,password)
        sftpclient= sshclient.open_sftp()
        sftpclient.get(file,filepath)
    except Exception as e:
        print(f"Error: {e}")
    if sftpclient:
        sftpclient.close()
    if sshclient:
        sshclient.close()

user_input = input("Please type out Config file location")

varCreation(user_input)