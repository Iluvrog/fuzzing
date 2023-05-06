from ftplib import FTP
import src.writer as w

def connexion(port = 21, host = 'localhost'):
    try:
        return FTP(host,port)
    except:
        return None

def send_command(ftp, list_command, file_name = 'error.txt'):
    res = ""
    error = False
    for com in list_command:
            try:
                res += ftp.sendcmd(com) + "\n"
            except:
                # if error -> save to file ?
                w.write_error("Command fail : " + com)
                error = True
    return res, error