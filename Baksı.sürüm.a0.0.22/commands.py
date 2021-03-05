# -*- coding: utf-8 -*-

#module's---------------------------------------------
import webbrowser as wb
import os
from gtts import gTTS
import playsound as pl
import random
import sys
import speech_recognition as sr
import functions as fk
import sys
import datetime as tm
import time
import subprocess
from pathlib import Path
import urllib.request
import json
import requests
from lxml import html
import speedtest

#variables--------------------------------------------

root_dir = Path("~").expanduser()

#-----------------------------------------------------


class komutlar(object):

#website's-----------------------------

    def youtube(self):
        wb.open('https://www.youtube.com')
        fk.konus("Youtube açılıyor")
    
    def facebook(self):
        wb.open('https://www.facebook.com')
        fk.konus("facebook açılıyor")

    def instagram(self):
        wb.open("https://www.instagram.com")
        fk.konus("instagram açılıyor")

    def eksisozluk(self):
        wb.open("https://eksisozluk.com")
        fk.konus("Ekşi açılıyor")

    def wikipedia(self):
        wb.open("https://www.wikipedia.com")
        fk.konus("Wikipedi açılıyor")

    def twitter(self):
        wb.open("https://www.twitter.com")
        fk.konus("Twitter açılıyor")

    def reddit(self):
        wb.open("https://www.reddit.com")
        fk.konus("Reddit açılıyor")
        
    def LinkedIn(self):
        wb.open("https://tr.linkedin.com")
        fk.konus("Linked in açılıyor")
    
    def eba():
        wb.open("https://www.eba.gov.tr/#/anasayfa")
        fk.konus("eba açılıyor")
    
    def eokul(self):
        wb.open("https://eokulyd.meb.gov.tr")
        fk.konus("E okul açılıyor")
    
    def edevlet(self):
        wb.open("https://giris.turkiye.gov.tr/Giris/")
        fk.konus("E devlet açılıyor")
    
    def haydArakınet(self):
        wb.open("http://haydarakin.meb.k12.tr")
        fk.konus("Haydar akın web adresi açılıyor")
    
    def Netflix(self):
        wb.open("https://www.netflix.com/tr/")
        fk.konus("Netflix açılıyor")
    
    def Amazon(self):
        wb.open("https://www.amazon.com.tr")
        fk.konus("Amazon açılıyor")
    
    def aliexpress(self):
        wb.open("https://tr.aliexpress.com")
        fk.konus("Aliexpress açılıyor")
    
    def hepsiburada(self):
        wb.open("https://www.hepsiburada.com")
        fk.konus("Hepsi burada açılıyor")
        
    def n11(self):
        wb.open("https://www.n11.com")
        fk.konus("n11 açılıyor")
        
    def teknosa(self):
        wb.open("https://www.teknosa.com/?gclid=EAIaIQobChMI1f2cvNeI7wIVFNZ3Ch0_xQLjEAAYASAAEgLRLPD_BwE&gclsrc=aw.ds")
        fk.konus("Teknosa açılıyor")
        
    def vatanpc(self):
        wb.open("https://www.vatanbilgisayar.com")
        fk.konus("Vatan bilgsayar açılıyor")
        
    def trendyol(self):
        wb.open("https://www.trendyol.com")
        fk.konus("trendyol açılıyor")
    
    
    
#----------------------------
      
    def pcoff(self):
        
        os.system("shutdown /s /t 1")
      
    def systemoff(self):
        fk.konus("sistem kapatılıyor")
        time.sleep(3)
        sys.exit()

    def wtime(self):
        saat = tm.datetime.now().strftime("%H:%M:%S")
        fk.konus(saat)    

    def searchingoogle(self):
        arama = fk.kayıt("ne aramak istiyorsun ?")
        url =  "https://www.google.com/search?q=" + arama
        wb.get().open(url) 
        a=(f"bunu arattım{arama}")
        fk.konus(a)

    def openvideo(self):
        arama= fk.kayıt("Hangi videoyu açmak istiyorsun")
        url= "https://www.youtube.com/results?search_query="+arama
        wb.get().open(url)
        a = (f"bu videoyu arattım{arama}")
        fk.konus(a)

    def weather(self):
        fk.hava_durumu()

    def internetspeed(self):
        saf_hız_indirme = speedtest.Speedtest().download()
        saf_hız_yukleme = speedtest.Speedtest().upload()
        yuvarlanmıs_hız_indirme = round(saf_hız_indirme)
        yuvarlanmıs_hız_yukleme = round(saf_hız_yukleme)
        son_hız_indirme= yuvarlanmıs_hız_indirme / 1e+6
        son_hız_yukleme = yuvarlanmıs_hız_yukleme / 1e+6
    
        yazı = f"""
            İndirme(Download) hızı {son_hız_indirme} mb/s
            Yükleme(Upload) hızı {son_hız_yukleme} mb/s
            """
        fk.konus(yazı)
    
    def coronavirus(self):
        r = requests.get("https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr&mid=%2Fm%2F01znc_")

        tree = html.fromstring(r.content)


        dailycases = tree.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]')
        vaccine = tree.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/div[1]/div[3]/div/div[1]/div[2]')
        totalcases =tree.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]')
        #dailytest =tree.xpath('')

        from datetime import date
        bugün = date.today()
        a = dailycases[0].text
        c = vaccine[0].text
        d = totalcases[0].text
        
        konus(bugün)
        konus("Tarihli vaka sayısı")
        konus(dailycases[0].text)
        konus("Türkiyedeki toplam vaka sayısı")
        konus(totalcases[0].text)
        konus("Toplam aşılama")
        konus(vaccine[0].text)
       
    
    def locationsearch(self):
        arama=fk.kayıt("Aranacak konumu söyleyiniz")
        url = "www.google.com/maps/search/"+ arama+"/"
        wb.get().open(url)
        a = (arama+"Konumu aratılmıştır")
        fk.konus(a)
        
    def opencontrol(self):
        os.startfile('C:\\Windows\\System32\\control.exe')
        fk.konus("denetim masasını açtım")

    def opencmd(self):
        os.startfile('C:\\Windows\\System32\\cmd.exe')
        fk.konus("cmd yi açtım")
    
    def opencalc(self):
        os.startfile('C:\\Windows\\System32\\calc.exe')
        fk.konus("Hesap makinesini açtım")
        
    def openmspaint(self):
        os.startfile('C:\\Windows\\System32\\mspaint.exe')
        fk.konus("paint i açtım")

    def openotepad(self):
        os.startfile('C:\\Windows\\System32\\notepad.exe')
        fk.konus("not defterini açtım")

    def exchance(self):
        rd = requests.get("https://www.bloomberght.com/doviz/dolar")
        re = requests.get('https://www.bloomberght.com/doviz/euro')
        rau =requests.get('https://www.anlikaltinfiyati.com/1-kilo-altin-bugun-ne-kadar.html')


        treed = html.fromstring(rd.content)
        treeeu =html.fromstring(re.content)
        treeau = html.fromstring(rau.content)


        kur_dolar = treed.xpath('/html/body/div[1]/section/div/div/div[1]/div[2]/div[1]/h1/span[1]')
        kur_euro = treeeu.xpath('/html/body/div[1]/section/div/div/div[1]/div[2]/div[1]/h1/span[1]')
        kur_gold = treeau.xpath('//*[@id="value_1-kilo"]')


        konus("dolar Türk lirası kuru ")
        konus(kur_dolar[0].text)
        konus("euro Türk lirası kuru ")
        konus(kur_euro[0].text)
        konus("1 kilogram altın ise")
        konus(kur_gold[0].text)
        konus("Türk lirası")


    def cryptocurrency_exchange(self):
        price_btc,btc = cryptocompare.get_price('BTC', 'USD'),"BTC" 
        cryptocompares(price_btc,btc)
        
        price_eth,eth = cryptocompare.get_price('ETH', 'USD'),"ETC"
        cryptocompares(price_eth,eth)
        
        price_ltc,ltc = cryptocompare.get_price('LTC', 'USD'),"LTC"
        cryptocompares(price_ltc,ltc)
        
        price_xrp,xrp = cryptocompare.get_price('XRP', 'USD'),"XRP"
        cryptocompares(price_xrp,xrp)
            
            
#-----------------------------------------------------



    def komutal(self,ses):
        if  "merhaba" in ses:
            print("Merhaba")
            
        elif  "youtube" in ses:
           self.youtube()

            
        elif "facebook" in ses:
            self.facebook()

            
        elif "instagram" in ses:
            self.instagram()
        
        
        elif "sistemi kapat" in ses:
            self.systemoff()
        
        elif "bilgisayarı kapat" in ses:
            self.pcoff()
        
        elif "saat kaç" in ses:
            self.wtime()

            
        elif "wikipedia" in ses:
            self.wikipedia()
        
        
        elif "twitter" in ses:
            self.twitter()
            
        
        elif "arama yap"in ses:
           self.searchingoogle()
        
        
        elif "video aç" in ses:
            self.openvideo()

            
        elif "cmd" in ses:
            self.opencmd()        
        
            
        elif "hava durumu" in ses:
            self.weather()
            
                
        elif "konum ara"in ses:
            self.locationsearch()
        
            
        elif "ekşi sözlük" in ses:
            self.eksisozluk()

        
        elif "denetim masası" in ses:
            self.opencontrol()
        
        
        elif "borsa" in ses:
            self.exchance()
        
        
        elif "kripto para" in ses:
            self.cryptocurrency exchange()
        

        elif "hesap makinesi" in ses:
            self.opencalc()


        elif "paint" in ses:
            self.openmspaint()


        elif "not defteri" in ses:
            self.openotepad()
        
        
        elif "eba" in ses:
            self.eba() 
        
        
        elif "e okul" in ses:
            self.eokul()
        
        
        elif "e devlet" in ses:
            self.edevlet()
        
        
        elif "haydar akın " in ses:
            self.haydArakınet()
        
        
        elif "netflix" in ses:
            self.Netflix()
        
        
        elif "amazon" in ses:
            self.Amazon()
        
        
        elif "aliexpress" in ses:
            self.aliexpress()
        
        
        elif "hepsi burada" in ses:
            self.hepsiburada()


        elif "n 11" or "n on bir" in ses:
            self.n11()

        
        elif "teknosa" in ses:
            self.teknosa()
        
        
        elif "vatan bilgisayar" in ses:
            self.vatanpc()
        
        
        elif "trendyol" in ses:
            self.trendyol()
            
        
        elif "vaka sayıları" in ses:
            self.coronavirus()
        
        else:
            print("_-")
            


