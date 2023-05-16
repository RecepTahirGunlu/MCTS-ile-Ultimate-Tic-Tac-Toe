# Ultimate Tic-Tac-Toe

Bu proje, Ultimate Tic-Tac-Toe oyununu ve MCTS (Monte Carlo Tree Search) algoritmasını içerir. İşte oyunun ve algoritmanın detaylı açıklamaları:

## Ultimate Tic-Tac-Toe Nedir?

Ultimate Tic-Tac-Toe, geleneksel 3x3 Tic-Tac-Toe oyununun bir genişlemesidir. Oyun, 3x3 büyük karelere ayrılmış 3x3 küçük karelerden oluşur. Amaç, küçük kareleri kazanarak büyük karelerde üstünlük sağlamaktır. Oyuncular, sırayla küçük karelere X veya O işaretlerini yerleştirirler. Ancak, bir oyuncunun hamlesini yapabilmesi için, sırası geldiğinde oynanması gereken küçük karenin belirlenmesi gerekmektedir. Eğer bir oyuncu, küçük kareyi kazanırsa, o küçük kareyi belirleyen büyük karede X veya O işareti yerleştirebilir. Oyun, tüm küçük kareleri dolduran veya büyük karelere üstünlük sağlayan oyuncu tarafından kazanılır.

## MCTS (Monte Carlo Tree Search) Nedir?

MCTS, belirsizlik içeren karar verme problemlerinde kullanılan bir arama algoritmasıdır. Bu algoritma, rastgele simülasyonlar yaparak oyun ağacını keşfeder ve en iyi hamleyi belirlemek için bir puanlama sistemini kullanır. MCTS, dört ana adımdan oluşur:

1. Seçim (Selection): Ağacın keşfedilmesi için uygun bir düğüm seçilir.
2. Genişleme (Expansion): Seçilen düğümün çocukları oluşturulur.
3. Simülasyon (Simulation): Seçilen düğümün çocuklarından birini rastgele seçerek simülasyon yapılır.
4. Geriye Yayılım (Backpropagation): Elde edilen sonuç, düğüm ve üst düğümlere geri yayılır.

Bu döngü, belirli bir süre veya hamle sayısı sınıra ulaşana kadar tekrarlanır ve sonunda en iyi hamle bulunur.

## Proje İçeriği

Bu proje, Ultimate Tic-Tac-Toe oyununu oynamanıza ve MCTS algoritmasını kullanarak bilgisayara karşı oynamanıza olanak sağlar. İşte proje içeriği ve bileşenleri:

1. `UltimateTicTacToe.py`: Ultimate Tic-Tac-Toe oyununun ana oyun motoru.
2. `mcts.py`: MCTS algoritmasının uygulandığı dosya.
3. `main.py`: Oyunun başlatıldığı ana dosya.

Nasıl Kullanılır?
1. Bu projeyi bilgisayarınıza klonlayın veya indirin.
2. main.py dosyasını çalıştırarak oyunu başlatın.
3. Oyun başladığında, sıra size geldiğinde bir hamle yapmanız gerekecektir.
4. Bilgisayarın hamle yapmasını bekleyin.
5. Oyun devam ederken, MCTS algoritması kullanılarak bilgisayarın en iyi hamleleri belirlenecektir.
6. Oyun, bir oyuncunun kazanması, berabere kalması veya sona ermesiyle sonuçlanana kadar devam eder.
Not: Bilgisayarın zorluğunu arttırmak için `mcts.py` dosyası içindeki MCTS classının arama fonksiyonunda yer alan iteration değişkenini değiştirebilirsiniz. Bilgisayarın zorluğu ile oynama süresi doğru orantılıdır.

[Download Exe File](https://github.com/RecepTahirGunlu/MCTS-ile-Ultimate-Tic-Tac-Toe/blob/master/download%20exe/main.exe)

