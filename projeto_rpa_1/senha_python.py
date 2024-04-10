import pyautogui
import time
import keyboard
import keyring

from getpass import getpass

service_id = 'LoginRPA'

print('Informe senha challenge')

senha_acc = getpass()

keyring.set_password(service_id, 'ChaveSecretaPython', senha_acc)