import speech_recognition as sr

import os
from gtts import gTTS
import random
import playsound as pl
import sys
import urllib.request
import json
import requests
from lxml import html


r  =  sr.Recognizer()


def speak(yazıverisi):
    
    sesverisi = gTTS(text=yazıverisi, lang='eng')
    rastgele = random.randint(1,100000)
    dosya = "ses--"+str(rastgele)+".mp3"
    sesverisi.save(dosya)
    pl.playsound(dosya)
    os.remove(dosya)



def konus(yazıverisi):
    
        
    sesverisi = gTTS(text=yazıverisi, lang='tr')
    rastgele = random.randint(1,100000)
    dosya = "ses--"+str(rastgele)+".mp3"
    sesverisi.save(dosya)
    pl.playsound(dosya)
    os.remove(dosya)
        
   


def kayıt( sorgu = False):
    try:
        with sr.Microphone() as kaynak:
            if sorgu:
                print(sorgu)
                konus(sorgu)
            r.adjust_for_ambient_noise(kaynak)
            ses = r.listen(kaynak)
            
            soz = ""
            
            
            soz = r.recognize_google(ses,language="tr-tr")
        
    except sr.UnknownValueError:
        print("ses algınlanamadı")
        
    except sr.RequestError:
        print("sistem çalışmıyor")
    
            
    return soz

def hava_durumu():
    r = requests.get("https://www.ntvhava.com")

    tree = html.fromstring(r.content)
    
    
    derece = tree.xpath('//*[@id="main"]/section[3]/div[1]/div[1]/ul[1]/li[2]/p[6]')
    konum  = tree.xpath('//*[@id="main"]/section[3]/div[1]/div[1]/ul[1]/li[2]/p[1]') 
    durum  = tree.xpath('//*[@id="main"]/section[3]/div[1]/div[1]/ul[1]/li[2]/p[4]')
    
    konus("Konum ")
    konus(konum[0].text)
    konus("Hissedilen sıcaklık")
    konus(derece[0].text)
    konus("Durum")
    konus(durum[0].text)
    
    

        
        
        
def run():
    
    while f:
        a = komutlar()
        ses = kayıt()
        ses = ses.lower()
        
       
        selamlamalar = ["uyan","selam","selamın aleyküm","naber","uyku modundan çık","merhaba",]
            
        if ses in selamlamalar:
            a.komutal(ses)
        
        
              
        else:
            pass
                
                 
                              
        

    
        
   

def cryptocompares(price,cryptocoin):
    import cryptocompare
    rd = requests.get("https://www.bloomberght.com/doviz/dolar")
    treed = html.fromstring(rd.content)
    kur_dolar = treed.xpath('/html/body/div[1]/section/div/div/div[1]/div[2]/div[1]/h1/span[1]')

    a = price.items()
    
    for i in a :
        b = list(i)[1]
        b = b.items()
        for i in b :
            i = list(i)
            parabirimi = i[0]
            değer = i[1]
            kur_dolar =kur_dolar[0].text
            kur_dolar = kur_dolar.replace(",",".")
            print(kur_dolar)
            tl_değer=değer*float(kur_dolar)
            tl_değer = int(tl_değer)
            değer = int(değer)
            konusma_metni=f"{cryptocoin} {parabirimi} karşılığı anlık olarak {değer}, Türk lirası olarak {tl_değer}"
            konus(konusma_metni)         
            