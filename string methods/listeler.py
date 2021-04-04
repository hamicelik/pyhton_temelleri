# list1=['bir','iki','üç',5,5.3,True]
# list2=['dörrt','beş','altı']
# print(list1+list2)
# print(type(list1))

#    ÖRNWK UYGULAMA ÇALIŞMASI

# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
araclar= ['Bmw','Mercedes','Opel','Mazda']
# print(araclar)

# # 2- Liste Kaç elemanlıdır ?
# print(len(araclar))

# 3- Listenin ilk ve son elemanı nedir ?
# print(araclar[0]+araclar[len(araclar)-1].center(10))

# 4- Mazda değerini Toyota ile değiştir
# araclar[-1]='toyata'
# print(araclar)

# 5- Mercedes listenin bir elemanı mıdır ?
# for i in araclar: 
#     if(i == 'Mercedes') : 
#         print ("Aranan Değer Mevcut")

# Listenin -2 indeksindeki değer nedir ?
# araclar1=araclar[-2]
# print(araclar1)

# 7- Listenin ilk 3 elemanını alın.
# araclar=araclar[0:3]
# print(araclar)

# 8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

# araclar[-2:]='Totoya','Renault'
# print(araclar)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# araclar[len(araclar):]='Audi','Nissan'
# print(araclar)

# 10- Listenin son elemanını silin.
# del araclar[-1]
# print(araclar)
# 11- Liste elemanlarını tersten yazdırınız.

# print(araclar[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

# studentA='Yiğit Bilgi',2010, (70,60,70)

# studentB='Sena Turan', 1999, (80,80,70)

# studentC='Ahmet Turan', 1998, (80,70,90)
# student=[studentA,studentB,studentC]
# print(student)

