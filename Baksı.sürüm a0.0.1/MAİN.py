import speech_recognition as sr
from COMMANDS import Komut
from COMMANDS import konuş
import time
from gtts import gTTS
import os

import playsound as pl


r = sr.Recognizer()

konuş("Uyku modundan Çıkmak İçin Yazan kelimeleri söyleyin")

print("uyku modundan çıkartmak için Merhaba/Günaydın/Uyan/Selam/Selamınaleyküm/Wake Up kelimelerini kullan")




    
try :
        
    with sr.Microphone() as kaynak:
        r.adjust_for_ambient_noise(kaynak)
        konuş("Arka plan gürültüsü:" + str(r.energy_threshold))
        while True:
            ses = r.listen(kaynak,)
            
            veri = ""
                  
            veri = r.recognize_google(ses,language="tr-tr")
            print(veri)
            g = Komut(veri)
            g.calıs()
                        
            
except sr.UnknownValueError:
        
    print("anlamadım")
            
except sr.WaitTimeoutError:
        
    print("tekrar et")
