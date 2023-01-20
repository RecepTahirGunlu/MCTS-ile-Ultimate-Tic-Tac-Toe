

import math
import random

class Dugum():
    def __init__(self, tahta, ebeveyn):
        self.tahta = tahta
        
        if self.tahta.kazandi_mi() or self.tahta.berabere_mi():
            self.terminal = True
        else:
            self.terminal = False       
        
        self.tamamen_genisledi_mi = self.terminal
        self.ebeveyn = ebeveyn
        self.ziyaret = 0
        self.skor = 0
        self.cocuk = {}

class MCTS():

    def arama(self, ilk_durum):
        self.kok = Dugum(ilk_durum, None)
        for yineleme in range(25):
            dugum = self.secim(self.kok)
            skor = self.simulasyon(dugum.tahta) 
            self.geriyayilim(dugum, skor)
        
        try:
            return self.en_iyi_hamleyi_al(self.kok, math.sqrt(2))
        except:
            pass
 
    def secim(self, dugum): 
        while not dugum.terminal:

            if dugum.tamamen_genisledi_mi:
                dugum = self.en_iyi_hamleyi_al(dugum, math.sqrt(2))
            else:
                return self.genisle(dugum)  
        return dugum

    def genisle(self, dugum):  
        durumlar = dugum.tahta.durumlar_olustur()     
        for durum in durumlar:

          if str(durum.pozisyon) not in dugum.cocuk:
                yeni_dugum = Dugum(durum, dugum)              
                dugum.cocuk[str(durum.pozisyon)] = yeni_dugum               
 
                if len(durumlar) == len(dugum.cocuk):
                    dugum.tamamen_genisledi_mi = True      
  
                return yeni_dugum

    def simulasyon(self, tahta):
        while not tahta.kazandi_mi():
            try:
                tahta = random.choice(tahta.durumlar_olustur()) 
                
            except:
                return 0 
        
        if tahta.oyuncu_2 == 'x': return 1 
        elif tahta.oyuncu_2 == 'o': return -1 

    def geriyayilim(self, dugum, skor): 
        while dugum is not None:
            dugum.ziyaret += 1
            dugum.skor += skor
            dugum = dugum.ebeveyn

    def en_iyi_hamleyi_al(self, dugum, kesif_sabiti):
        en_iyi_skor = float('-inf')
        en_iyi_hamleler = []

        for cocuk_dugum in dugum.cocuk.values():

            if cocuk_dugum.tahta.oyuncu_2 == 'x': mevcut_oyuncu = 1
            elif cocuk_dugum.tahta.oyuncu_2 == 'o': mevcut_oyuncu = -1 
            
            hamle_skor = mevcut_oyuncu * cocuk_dugum.skor / cocuk_dugum.ziyaret + kesif_sabiti * math.sqrt(math.log(dugum.ziyaret / cocuk_dugum.ziyaret)) 
            
            if hamle_skor > en_iyi_skor:
                en_iyi_skor = hamle_skor
                en_iyi_hamleler = [cocuk_dugum]            
            elif hamle_skor == en_iyi_skor:
                en_iyi_hamleler.append(cocuk_dugum)                 
        return random.choice(en_iyi_hamleler)
