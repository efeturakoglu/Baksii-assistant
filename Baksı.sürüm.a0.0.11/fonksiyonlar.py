import speech_recognition as sr
from playsound import playsound as pl
import os
from gtts import gTTS
import random
import playsound as pl
import sys
from tkinter import *
from Komutlar import*


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
    
    with sr.Microphone() as kaynak:
        if sorgu:
            print(sorgu)
            konus(sorgu)
        r.adjust_for_ambient_noise(kaynak)
        ses = r.listen(kaynak)
        
        soz = ""
        
        try:
            soz = r.recognize_google(ses,language="tr-tr")
        
        except sr.UnknownValueError:
            print("ses algınlanamadı")
        
        except sr.RequestError:
            print("sistem çalışmıyor")
            konus("sistem çalışmıyor, Galiba internet yok")
            
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
    