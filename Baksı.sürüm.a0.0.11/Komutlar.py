import webbrowser as wb
import os
from gtts import gTTS
import playsound as pl
import random
import sys
import speech_recognition as sr
import fonksiyonlar as fk
import sys
import datetime as tm
import time
import subprocess
from pathlib import Path
import urllib.request
import json
import requests
from lxml import html
#-----------------------------------------------------

root_dir = Path("~").expanduser()

#-----------------------------------------------------


def komutlar(ses):
    if  "merhaba" in ses:
        print("Merhaba")
        
    elif  "youtube" in ses:
        wb.open('https://www.youtube.com')
        fk.konus("Youtube açılıyor")

        
    elif "facebook" in ses:
        wb.open('https://www.facebook.com')
        fk.konus("facebook açılıyor")

        
    elif "instagram" in ses:
        wb.open("https://www.instagram.com")
    
    
    elif "sistemi kapat" in ses:
        fk.konus("sistem kapatılıyor")
        time.sleep(3)
        sys.exit()
    
    
    elif "saat kaç" in ses:
        saat = tm.datetime.now().strftime("%H:%M:%S")
        fk.konus(saat)

        
    elif "wikipedia" in ses:
        wb.open("https://www.wikipedia.com")
        
    
    elif "arama yap"in ses:
        arama = fk.kayıt("ne aramak istiyorsun ?")
        url =  "https://www.google.com/search?q=" + arama
        wb.get().open(url)
        a=(" bunu arattım"+ arama)
        fk.konus(a )
     
    
    elif "video aç" in ses:
        arama= fk.kayıt("Hangi videoyu açmak istiyorsun")
        url= "https://www.youtube.com/results?search_query="+arama
        wb.get().open(url)
        a = ("bu videoyu arattım"+ arama)
        fk.konus(a)

        
    elif "cmd" in ses:
        os.startfile('C:\\Windows\\System32\\cmd.exe')
        fk.konus("cmd yi açtım")        
    
        
    elif "hava durumu" in ses:
        
        fk.hava_durumu()
        
            
    elif "konum ara"in ses:
        arama=fk.kayıt("Aranacak konumu söyleyiniz")
        url = "www.google.com/maps/search/"+ arama+"/"
        wb.get().open(url)
        a = (arama+"Konumu aratılmıştır")
        fk.konus(a)
    
    
    elif "twitter" in ses:
        wb.open("https://www.twitter.com")
        
        
    elif "ekşi sözlük" in ses:
        wb.open("https://eksisozluk.com")

    
    
    
    
    else:
        print("_-")
        
        