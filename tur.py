# Criado por: Juan Santos Trigo Nasser
# Versão: 1.0
# Data 13/08/2023

# imports
import pyautogui as bot
import time

# definir variaveis
abrir_peruibetur = True
i = 0


# para exportar para exe: pyinstaller --noconfirm --onefile --console bot.py 
bot.FAILSAFE = True
bot.PAUSE = 1
print("INFO: Para forçar parada, pouse o mouse no canto superior esquerdo do monitor")
print("ALERTA: Iniciando automatização em 2 segundos, não mova o mouse")
time.sleep(2)
print("ALERTA: Automatização iniciada!")

# colocar comandos a partir daqui
# entrando no site peruibetur
if abrir_peruibetur == True:
    bot.hotkey("win", "r")
    bot.write("https://peruibetur.com.br/")
    bot.press("enter")
    time.sleep(10)
    bot.PAUSE = 0.3
    while i < 4:
        bot.press("tab")
        i +=1
    i = 0
    bot.press("enter")
    time.sleep(10)
    while i < 4:
        bot.press("tab")
        i +=1
    i = 0
    bot.press("enter")
    time.sleep(10)
else:
    print("ALERTA: Abra o chrome em 5 segundos!")
    time.sleep(5)

