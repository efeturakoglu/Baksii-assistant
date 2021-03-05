from functions import*
from commands import*
import speech_recognition as sr
from playsound import playsound as pl


"""
Sürüm notları;

-Program sözdiziminde düzeltmeler.
-Yeni fonksiyonlar.
-OOP(object oriented programming).

Programcı -- Efe Turakoğlu
Sınıf  -- 10/A
Numara -- 604
Okul   -- Haydar Akın Mesleki ve Teknik Anadolu Lisesi
Öğretmen -- Nural Kahraman

"""


if __name__ == '__main__':
    konus("Merhaba Sahip")
    f = True
    while f:
        a = komutlar()
        ses = kayıt()
        ses = ses.lower()
        a.komutal(ses)
        print(ses)
                
       
    