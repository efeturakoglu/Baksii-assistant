import speech_recognition as sr
import sys
import time
import os
import webbrowser as wb
import playsound as pl
from gtts import gTTS
import random

a = True


yazı = "sürüm = alfa 0.0.1,Proje Sahibi = Efe Turakoğlu,Okul no = 604 Okul İsimi = Haydar Akın Mesleki ve Teknik Anadolu Lisesi"




r = sr.Recognizer()

def konuş(yazıverisi):
    sesverisi = gTTS(text=yazıverisi, lang='tr')
    rastgele = random.randint(1,100000)
    dosya = "ses--"+str(rastgele)+".mp3"
    sesverisi.save(dosya)
    pl.playsound(dosya)
    os.remove(dosya)


class Komut():
    
    def __init__(self,gelenses):
        self.ses = gelenses.upper()
        self.seslistesi = self.ses.split()
        self.Komutlar = ["SAAT","NABER","KAPAT","YOUTUBE","FACEBOOK","İNSTAGRAM","SORGULA","ARA","HAKKINDA","BİLGİ","CMD","ZOOM","DENETİM"]
        self.komutlar2 = ["UYAN","GÜNAYDIN","MERHABA","SELAMINALEYKÜM","WAKE UP","SELAM"]
        
    def close(self):
        sys.exit()
            
    def youtube(self):
        wb.open('https://www.youtube.com')
    
    
    def sohbet(self):
        pass
    
    def havadurumu(self):
        pass
    
    def saat(self):
        pass

    def pckapat(self):
        pass
    
    def accmd(self):
        os.system("cmd.exe")
    
    def aczoom(self):
        os.system("Zoom.exe")

    def facebook(self):
        wb.open('https://www.facebook.com')
    
    def instagram(self):
        wb.open('https://www.instagram.com')
    
    def denetimm(self):
        os.system("control.exe")
    
    def hakkında(self):
        return konuş(yazı)
        
    def sistemkonfig(self):
        pass
    
    def haberler(self):
        pass
    
    def yazdır(self):
        print("yutup")
        
    def komutbul(self):
        for komut in self.Komutlar:
            if komut in self.seslistesi:
                self.komutcalıstır(komut)
                
                  
    def calıs(self):
        for komut in self.komutlar2:
            if komut in self.seslistesi:
                self.run(komut)
                
                
                
    def run(self,komut):
        print("Uyku modundan çıkıldı")
        konuş("Uyku modundan çıkıldı")
        
        try :
            while  a:
            
                with sr.Microphone() as kaynak:
                    r.adjust_for_ambient_noise(kaynak)
                    ses = r.listen(kaynak)
                    
                    komut = ""
                          
                    komut = r.recognize_google(ses,language= "tr-TR")
                    print(komut)
                    g = Komut(komut)
                    g.komutbul()
                
        except sr.UnknownValueError:
                print("ne dediğini anlayamadım")
                konuş("ne dediğini anlamadım")
                konuş("uyku moduna girildi")
                    
        except sr.WaitTimeoutError:
                konuş("yeniden komut vermek için günaydın de")
                konuş("uyu moduna girildi")

        
    def komutcalıstır(self,komut):
        
        if komut == "KAPAT":        
            self.close()
            
        elif komut == "YOUTUBE":
            self.youtube()
        
        elif komut == "İNSTAGRAM":
            self.instagram()
            
        elif komut == "FACEBOOK":
            self.facebook()
            
        elif komut =="SORGULA" :
            
            kelimeler = self.seslistesi
            endeks = kelimeler.index("SORGULA")
            aranan = ""
            i = endeks + 1
            while i < len(kelimeler):
                aranan +=" " + kelimeler[i]
                i +=1
            print("sorgu = ", aranan)
            konuş("Aratılıyor")
            konuş(aranan)
            wb.open("https://yandex.com.tr/search/?text='{}'".format(aranan))
            
               
        elif komut == "HAKKINDA":
            self.hakkında()
            
        elif komut == "BİLGİ":
            self.hakkında()
            
        elif komut =="CMD":
            print("cmd açılıyor")
            self.accmd()
            
        elif komut=="DENETİM":
            self.denetimm()
            
        elif komut == "ZOOM":
            self.aczoom()
            
        elif komut == "UYU":
            global a
            a = False
            