#deneme= "bu Yazı .string Methotlarını denemek amaçlıdır     "
# deneme= deneme.upper()        #bütün harfleri büyük harfle yazdırır.
# print(deneme)    
# deneme= deneme.title()  #her kelime baş harfi büyük harfle yazılır.
# print(deneme)
# deneme= deneme.capitalize()  #sadece cümlenin en başındaki kelimenin ilk harfi büyük olur.
# print(deneme)
# deneme= deneme.strip()  #parola aldığımız alanlarda işimize yarayabilir.Baştaki boşluğu almaz.Kapatır
# print(deneme) 
# #deneme= deneme.split() # ****ÖNEMLİ cümledeki her bir kelimeyi dizi elemanı olarak ayırır.
# #print(deneme)
# deneme= deneme.split('.') # parantez içerisinde verdiğimiz ifadeye göre  ayırır
# print(deneme)
# deneme= ' '.join(deneme) # yukarıda dizi elemanlarına ayırdığımız cümleyi tekrar birleştirmeye yarar.Ben burada boşluk koyarak ekle dedim ama herhangi bir paremetrede verebilirdim
# print(deneme)
# deneme= deneme.find('Methotlarını')  # içinde geçen bir kelimeyi aynen aramak şartı ile index numarası döndürür.
# print(deneme)
# isFound= deneme.startswith('d') # cümle 'd' ile başıyor mu sorduğumda  true yada false döndürüyor
# print(isFound)
# deneme= deneme.replace('Yazı','hami') # yazının içinde önce veriğimiz değeri bulu ve verdiğimiz ikinci paremetreyi yerleştirir.Örneğin türkçe harf uyumsuzluğu oldu replace('ç','c') burada ç yi c ile değiştirdik
# print(deneme)
# deneme1="çelik çomak ördek kalemlık"
# deneme1= deneme1.replace('ç','c').replace('ö','o').replace('ı','i')
# print(deneme1)

# deneme= deneme.center(100)  #Yer Tutucu(Placeholder) görevi görür. metni buna göre merkeze alır
# print(deneme)
# deneme= deneme.center(100,'*')  # ikinci paremetre kullanımı bu şekilde
# print(deneme)

deneme= 'armur hamsi elma istavrit hamsi bu ne kadar hamsi lan hamsi mi bu hamsi'
deneme= deneme.count('elma')
print(deneme)   #count saymak için kllanılan bir string methodu kullanım yollarından biri bu şekilde

# deneme=deneme.index('hamsi') 
# print(deneme)




