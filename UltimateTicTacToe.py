from copy import deepcopy
import random
from itertools import combinations
from mcts import *
import time

class Tahta:
    
    def __init__ (self, tahta =None ):
            self.oyuncu_1 = 'x'
            self.oyuncu_2 = 'o'
            self.alt_tahta = None
            self.bos_kare = '.'
            self.pozisyon = {}
            self.tahta_sira=[]
            self.init_tahta()
            self.sonraki_tahta = {(1,1):1, (1,2):2, (1,3):3, (2,1):4, (2,2):5, (2,3):6, (3,1):7, (3,2):8, (3,3):9}
            self.son_hamle = []
            if tahta is not None:
                self.__dict__= deepcopy(tahta.__dict__)

    def init_tahta(self):

        alt_tahtalar = [0,1,2,3,4,5,6,7,8]

        for poz in range(0,9,3):
            sira_1 = [[0,0], [0,1], [0,2], [0,0], [0,1], [0,2], [0,0], [0,1], [0,2]]
            sira_2 = [[1,0], [1,1], [1,2], [1,0], [1,1], [1,2], [1,0], [1,1], [1,2]]
            sira_3 = [[2,0], [2,1], [2,2], [2,0], [2,1], [2,2], [2,0], [2,1], [2,2]]          
            for j in range(9):  
                if j <3:
                    sira_1[j].insert(0, alt_tahtalar[poz]) 
                if j >=3 and j<6:    
                    sira_1[j].insert(0, alt_tahtalar[poz+1]) 
                if j>=6 and j <9:
                    sira_1[j].insert(0, alt_tahtalar[poz+2]) 
            self.tahta_sira+=sira_1
                    
            for j in range(9):
                if j <3:
                    sira_2[j].insert(0, alt_tahtalar[poz+0])
                if j >=3 and j<6:    
                    sira_2[j].insert(0, alt_tahtalar[poz+1])
                if j>=6 and j <9:
                    sira_2[j].insert(0, alt_tahtalar[poz+2])
            self.tahta_sira+=sira_2
            
            for j in range(9):
                if j <3:
                    sira_3[j].insert(0, alt_tahtalar[poz+0])
                if j >=3 and j<6:    
                    sira_3[j].insert(0, alt_tahtalar[poz+1])
                if j>=6 and j <9:
                    sira_3[j].insert(0, alt_tahtalar[poz+2])
            self.tahta_sira+=sira_3
            
        for ilk in range(len(self.tahta_sira)):
            self.pozisyon[self.tahta_sira[ilk][0], self.tahta_sira[ilk][1], self.tahta_sira[ilk][2]] = self.bos_kare


    def durumlar_olustur(self ):
        
        son_hamle = self.son_hamle
        kalan_tahtalar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        son_hamle = (son_hamle[1], son_hamle[2])
        for key, value in self.sonraki_tahta.items():
            if key == son_hamle:
                alt_tahta = value
                
        eylemler = []
        for  satir in range (3):
            for sutun in range(3):
                if self.pozisyon[alt_tahta-1, satir, sutun] == self.bos_kare:
                    eylemler.append(self.hamle_yap(alt_tahta, satir+1, sutun+1))
                    
        if len(eylemler) ==0:  
            kalan_tahtalar.remove(alt_tahta)
            for tahta in kalan_tahtalar:
                for  satir in range (3):
                    for sutun in range(3):
                        if self.pozisyon[tahta-1, satir, sutun] == self.bos_kare:
                            eylemler.append(self.hamle_yap(tahta, satir+1, sutun+1))
        
        return eylemler 

    def hamle_yap(self, alt_tahta, satir, sutun):

        tahta = Tahta(self)      
        if tahta.pozisyon[alt_tahta-1, satir-1, sutun-1] == self.bos_kare:
            tahta.pozisyon[alt_tahta-1, satir-1, sutun-1] = self.oyuncu_1
            (tahta.oyuncu_1, tahta.oyuncu_2) = (tahta.oyuncu_2, tahta.oyuncu_1) 
        
        return tahta

    def tahtayi_kilitle(self, kazanan_tahtalar):
        for tahta in kazanan_tahtalar:
            for satir in range(3):
                for sutun in range(3):
                    if not self.pozisyon[tahta-1, satir, sutun] == self.oyuncu_2:
                        self.pozisyon[tahta-1, satir, sutun] = self.oyuncu_2

    def oyuncu_sonraki_hamle(self, oyuncu_hamle, bot_hamle):

        oynanan_hamle = dict(bot_hamle - oyuncu_hamle)
        tahta_bul = False
        for key, value in oynanan_hamle.items():
            if value == 'o' or value == 'x':
                hmle = list(key)
                sonra = ((hmle[1])+1, (hmle[2])+1)
                
                for key, value in self.sonraki_tahta.items():
                    if sonra == key:
                        for satir in range(3):
                            for sutun in range(3):
                                if self.pozisyon[value-1, satir, sutun] == self.bos_kare:
                                    tahta_bul = True
                                    self.alt_tahta = value
                                    
        if tahta_bul == False: 
            print('Oynayacağınız alt tahtayı da seçiniz.')
            self.alt_tahta = None
            
        return 

    def kazandi_mi(self):        
        kazanan_pozisyonlar = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
        kazanan_tahtalar = []       #yatay kazanma#           #dikey kazanma#         #çapraz kazanma#
        for tahta in range(0,9):  
            #yatay kazanma
            for sutun in range(3):
                kazanma_sirasi = []
                for satir in range(3):
                    if self.pozisyon[tahta, satir, sutun] == self.oyuncu_2:
                        kazanma_sirasi.append((satir,sutun))
                    if len(kazanma_sirasi) == 3:
                        kazanan_tahtalar.append(tahta+1) 
            #dikey kazanma
            for satir in range(3):
                kazanma_sirasi = []
                for sutun in range(3):
                    if self.pozisyon[tahta, satir, sutun] == self.oyuncu_2:
                        kazanma_sirasi.append((satir,sutun))
                    if len(kazanma_sirasi) == 3:                  
                        kazanan_tahtalar.append(tahta+1)
            #soldan sağa çapraz kazanma 1-5-9     
            kazanma_sirasi=[]
            for satir in range(3):
                sutun = satir
                if self.pozisyon[tahta, satir, sutun] == self.oyuncu_2:
                    kazanma_sirasi.append((satir,sutun))
                if len(kazanma_sirasi) == 3:
                    kazanan_tahtalar.append(tahta+1)
            #sağdan sola çapraz kazanma 3-5-7       
            kazanma_sirasi= []
            for satir in range(3):
                sutun = 2- satir 
                if self.pozisyon[tahta, satir, sutun] == self.oyuncu_2:
                    kazanma_sirasi.append((satir,sutun))
                if len(kazanma_sirasi) == 3:
                    kazanan_tahtalar.append(tahta+1)       
        if len(list(set(kazanan_tahtalar))) >=1:  

            self.tahtayi_kilitle(list(set(kazanan_tahtalar)))       

        if len(list(set(kazanan_tahtalar))) >=3:       
            tahta_kombinasyonlari =  combinations(kazanan_tahtalar,3)    

            for komb in tahta_kombinasyonlari:
                komb = tuple(sorted(komb))

                if komb in kazanan_pozisyonlar:
                    return True               
        return False

    def berabere_mi(self):
        bos_alan = 0
        for tahta in range(0,9):
            for satir in range(3):
                for sutun in range(3):
                    if self.pozisyon[tahta, satir, sutun] == self.bos_kare:
                        bos_alan +=1
        if bos_alan >0: return False
        else: return True

    def game_loop(self):
        
        print("Çıkmak için 'çıkış' yazınız.")       
        print(self)
        mcts = MCTS()
        
        while True:

            if self.alt_tahta == None:
                kullanici = input('tahta, satır, sutun > ' )
            else: 
                print('Oynanabilir tahta: ',self.alt_tahta)
                kullanici = input('satır, sutun > ')
            if kullanici == 'çıkış':
                break
            if kullanici == '':
                continue

            try:
                if self.alt_tahta == None:
                    self.alt_tahta, satir, sutun = (map(int, kullanici.split(',')))
                else:
                    satir, sutun = map(int, kullanici.split(','))
                    
                self.son_hamle = [self.alt_tahta, satir, sutun]
                if self.pozisyon[self.alt_tahta-1, satir-1, sutun-1] == self.bos_kare:
                    self = self.hamle_yap(self.alt_tahta, satir, sutun)
                    oyuncu_hamle = self.pozisyon
                    print(self)
                    
                    print("\nBot düşünüyor...\n")
                    baslama_zamani = time.perf_counter()
                    oyuncu_hamle= set(oyuncu_hamle.items())
                    en_iyi_hamle = mcts.arama(self)  
                    bitis_zamani = time.perf_counter() - baslama_zamani
                    print('Oynama süresi', bitis_zamani)
                    
                    try:
                        self = en_iyi_hamle.tahta
                        bot_hamle = self.pozisyon
                        bot_hamle = set(bot_hamle.items())                   
                        
                    except :
                        pass

                    print(self)
                    self.oyuncu_sonraki_hamle(oyuncu_hamle, bot_hamle)
                    
                    if self.kazandi_mi():
                        print("Oyuncu '%s' kazandı." % self.oyuncu_2 )
                        break
                    elif self.berabere_mi():
                        print('Oyun berabere bitti.')
                        break

                else:
                    print('illegal hamle!')
                    continue
            
            except :
                print('Gecersiz girdi / illegal hamle ')  

    def __str__ (self ):

        tahta_string = '┏━━━━━━━┳━━━━━━━┳━━━━━━━┓\n┃'
        sayac = 0
        for ilk in range(len(self.tahta_sira)):
            if sayac > 0 and sayac %3 == 0 :
                tahta_string +=' ┃'
            if sayac > 0 and sayac %9 == 0:
                tahta_string += '\n┃'
            if sayac > 0 and sayac % 27 == 0:
                tahta_string += '━━━━━━━╋━━━━━━━╋━━━━━━━┫\n┃'
            tahta_string += ' %s' % self.pozisyon[self.tahta_sira[ilk][0], self.tahta_sira[ilk][1], self.tahta_sira[ilk][2]]
            sayac+=1
        tahta_string += ' ┃\n┗━━━━━━━┻━━━━━━━┻━━━━━━━┛\n'
        if self.oyuncu_1 == 'x':
            tahta_string = "\n ------------------------\n      x'in sirasi: \n ------------------------\n\n" + tahta_string
        elif self.oyuncu_1 == 'o':
            tahta_string = "\n ------------------------\n      o'nun sirasi: \n ------------------------\n\n" + tahta_string
        return tahta_string

if __name__ == '__main__':

    tahta = Tahta()          
    tahta.game_loop()
             
