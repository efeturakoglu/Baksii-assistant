from fonksiyonlar import*
from Komutlar import*
from tkinter import *


def run():
    
    while True:
        ses = kayıt()
        ses = ses.lower()
        komutlar(ses)

konus("Merhaba Sahip")

run()

