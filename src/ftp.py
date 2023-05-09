from ftplib import FTP
import src.writer as w

def connexion(port = '21', host = 'localhost'):
    try:
        co = FTP(host, port)
        co.login()
    except Exception as e:
        print("Erreur lors de la connexion:", e)
        w.write_error("Erreur lors de la connexion:" + str(e))
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