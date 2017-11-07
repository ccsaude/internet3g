##/usr/bin/python3.5 /home/agnaldo/PycharmProjects/ReportUpdaterPy/taskExecutor.py
from appJar import gui
import subprocess
import time
from subprocess import Popen, PIPE, STDOUT
import threading


# run the shell as a subprocess:
def beginconnection():
    cmd = 'wvdial > /opt/walout32.txt 2>&1'
    #print(shlex.split(cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)


def connect(button):

    app.infoBox("Informacao","Estabelecendo conexao...")
    time.sleep(5)
    devices = getmodemname()
    found = False
    for word in devices:
        if "ZTE WCDMA Technologies" in devices:
            app.setTextArea("txt_area", "")
            found = True
            break

    if found:
        app.setLabel("lbl_modem", "Modem: ZTE WCDMA Technologies")
        time.sleep(3)

        t1 = threading.Thread(target=beginconnection())
        t1.start()
        time.sleep(15)
        try:
            f = open('/opt/walout32.txt', encoding='utf-8', errors='ignore')
        except IOError:
            print('file not created yet')
        else:
            try:
                with f:
                    text = f.read()
                    app.setTextArea("txt_area", text)
                    if 'secondary DNS address 8.8.8.8' in text:
                        app.infoBox("Info", "Conectado a internet.")
                        #app.setButton("btn_conect", "Desconectar")
                    else:
                        app.infoBox("Info","Tentar novamente! veja os logs")

                #print(f.readlines())
                    f.close()
            except IOError:
                app.setTextArea("txt_area", "Aconteceu um erro ao conectar o medem. Desconectre o modem e volte a ligar")

        #with open('/opt/walout32.txt') as f:
         #  app.setTextArea("txt_area",f.read())

    else:
        app.warningBox("Erro","Nenhum modem encontrado, Ligue o modem no PC e agurade 15sec")
        app.setLabel("lbl_modem","Modem :")


# ###########################  Global variables & UI  #########################################
from appJar import gui

app=gui("Internet 3G Movitel")
app.setGeometry(700, 600)
app.setExpand("both")
app.setFont(14)
app.setSticky("nw")
app.setStretch("both")
app.addLabel("lbl_modem", "Modem :",0,0)
app.addButton("connect", connect, 1, 0)
#app.addButton("disconect", connect, 1, 0)
#app.addButton("reconect", connect, 1, 0)
app.setSticky("nwes")
app.addTextArea("txt_area",colspan=2,rowspan=1)                                         # #
app.addLabel("lbl_control")
                                                                                        # ##
# #############################################################################################
def getmodemname():
    modem = "Nenhum modem encontrado."
    try:
        cmd_result = subprocess.check_output("lsusb", bufsize=-1, shell=True)
    except subprocess.CalledProcessError as err:
        print("Error occurred trying to locate mysql installation dir.")
    else:
        #    cmd_result = subprocess.check_output("where mysql", bufsize=-1, shell=True)
        cmd_result =str(cmd_result.rstrip(), encoding='utf-8')
    return cmd_result


def main():
        app.go()


if __name__ == "__main__":
    main()
